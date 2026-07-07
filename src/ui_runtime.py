# ui_runtime.py
"""Runtime safety helpers for BK Video Encoder.

This module is intentionally small and dependency-light. It patches only the
main App instance at startup so the existing GUI can become smoother without a
large rewrite.
"""

from __future__ import annotations

import logging
import platform
import queue
import signal
import types
from typing import Any, Optional

import customtkinter as ctk

logger = logging.getLogger(__name__)

UI_QUEUE_BATCH_LIMIT = 32
UI_QUEUE_IDLE_TICK_MS = 16
ESTIMATE_DEBOUNCE_MS = 180
PREVIEW_DEBOUNCE_MS = 90
PROCESS_CANCEL_GRACE_SEC = 2.5


def install_runtime_guards(app: Any) -> None:
    """Install smooth-UI helpers on an App instance."""
    app._ui_queue_batch_limit = UI_QUEUE_BATCH_LIMIT
    app._ui_queue_idle_tick_ms = UI_QUEUE_IDLE_TICK_MS
    app._estimate_after_id = None
    app._preview_after_id = None
    app._active_toast = None

    app._process_ui_queue = types.MethodType(_process_ui_queue, app)
    app._request_estimate_update = types.MethodType(_request_estimate_update, app)
    app._request_preview_refresh = types.MethodType(_request_preview_refresh, app)
    app._show_toast = types.MethodType(_show_toast, app)
    app._terminate_process_tree = types.MethodType(_terminate_process_tree, app)


def _process_ui_queue(self: Any) -> None:
    """Drain a bounded number of callbacks per frame.

    The old loop drained the whole queue in one UI tick. During fast FFmpeg
    progress bursts or preview generation this can starve Tk's event loop. A
    bounded drain keeps the window responsive and lets Windows repaint/input
    events run between chunks.
    """
    processed = 0
    try:
        while processed < getattr(self, "_ui_queue_batch_limit", UI_QUEUE_BATCH_LIMIT):
            callback = self.ui_update_queue.get_nowait()
            if callable(callback):
                try:
                    callback()
                except Exception:
                    logger.exception("UI callback failed")
            processed += 1
    except queue.Empty:
        pass

    # If more callbacks are waiting, schedule the next chunk quickly; otherwise
    # use a 60fps-friendly idle cadence.
    try:
        delay = (
            1
            if not self.ui_update_queue.empty()
            else getattr(self, "_ui_queue_idle_tick_ms", UI_QUEUE_IDLE_TICK_MS)
        )
        if self.winfo_exists():
            self.after(delay, self._process_ui_queue)
    except Exception:
        logger.debug(
            "Stopped UI queue pump because the window is closing.", exc_info=False
        )


def _request_estimate_update(self: Any, delay_ms: int = ESTIMATE_DEBOUNCE_MS) -> None:
    """Debounce expensive estimate recalculation during typing/slider moves."""
    try:
        if getattr(self, "_estimate_after_id", None):
            self.after_cancel(self._estimate_after_id)
    except Exception:
        pass

    def _run() -> None:
        self._estimate_after_id = None
        if self.winfo_exists():
            self._update_estimates()

    self._estimate_after_id = self.after(delay_ms, _run)


def _request_preview_refresh(
    self: Any, image_path: Optional[str] = None, delay_ms: int = PREVIEW_DEBOUNCE_MS
) -> None:
    """Debounce preview redraws when crop fields/sliders change."""
    try:
        if getattr(self, "_preview_after_id", None):
            self.after_cancel(self._preview_after_id)
    except Exception:
        pass

    def _run() -> None:
        self._preview_after_id = None
        if not self.winfo_exists():
            return
        try:
            import gui_updaters

            gui_updaters.display_preview_image(self, image_path)
        except Exception:
            logger.exception("Preview refresh failed")

    self._preview_after_id = self.after(delay_ms, _run)


def _show_toast(self: Any, title: str, message: str, duration_ms: int = 2400) -> None:
    """Small non-blocking notification used for routine success messages."""
    try:
        if getattr(self, "_active_toast", None) and self._active_toast.winfo_exists():
            self._active_toast.destroy()
    except Exception:
        pass

    try:
        toast = ctk.CTkToplevel(self)
        self._active_toast = toast
        toast.overrideredirect(True)
        toast.attributes("-topmost", True)
        toast.configure(fg_color="#0E1117")
        frame = ctk.CTkFrame(
            toast,
            fg_color="#151A22",
            corner_radius=14,
            border_width=1,
            border_color="#DAB45B",
        )
        frame.pack(fill="both", expand=True, padx=1, pady=1)
        ctk.CTkLabel(
            frame, text=title, font=("Segoe UI", 13, "bold"), text_color="#F5F6F8"
        ).pack(anchor="w", padx=16, pady=(12, 0))
        ctk.CTkLabel(
            frame,
            text=message,
            font=("Segoe UI", 12),
            text_color="#A9B4C0",
            wraplength=360,
            justify="left",
        ).pack(anchor="w", padx=16, pady=(3, 12))
        self.update_idletasks()
        x = self.winfo_rootx() + max(24, self.winfo_width() - 430)
        y = self.winfo_rooty() + max(24, self.winfo_height() - 140)
        toast.geometry(f"400x92+{x}+{y}")
        toast.after(
            duration_ms, lambda: toast.destroy() if toast.winfo_exists() else None
        )
    except Exception:
        logger.info("Toast fallback: %s - %s", title, message)
        try:
            import gui_updaters

            gui_updaters.handle_status_update(self, f"{title}: {message}")
        except Exception:
            pass


def _terminate_process_tree(
    self: Any, process: Any, description: str = "process"
) -> None:
    """Terminate an FFmpeg process with Windows-aware escalation."""
    if not process or process.poll() is not None:
        return
    pid = getattr(process, "pid", "unknown")
    logger.info("Cancelling %s PID %s", description, pid)

    try:
        if platform.system() == "Windows":
            try:
                process.send_signal(signal.CTRL_BREAK_EVENT)
                logger.info("Sent CTRL_BREAK_EVENT to PID %s", pid)
            except Exception:
                process.terminate()
                logger.info("Sent terminate signal to PID %s", pid)
        else:
            process.terminate()
        try:
            process.wait(timeout=PROCESS_CANCEL_GRACE_SEC)
            return
        except Exception:
            pass
        if process.poll() is None:
            process.kill()
            logger.warning("Killed unresponsive %s PID %s", description, pid)
    except Exception:
        logger.exception("Failed to terminate %s PID %s", description, pid)

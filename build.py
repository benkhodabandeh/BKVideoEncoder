#!/usr/bin/env python3
"""Cross‑platform build script for Ben. Khodabandeh Video Encoder.

Assumes:
  - Python dependencies already installed (pip install -r requirements.txt pyinstaller)
  - bin/ is populated with FFmpeg + shared libs (or src/vmaf_v0.6.1.json at minimum)

Usage:
  python build.py
"""
import platform, shutil, subprocess, sys, tempfile  # fmt: skip
from pathlib import Path

ROOT = Path(__file__).parent.resolve()
DIST = ROOT / "dist"
BIN  = ROOT / "bin"
VER  = "2026.7.7"
NAME = "BKVideoEncoder"


def main():
    system = platform.system()

    # Clean previous build artifacts
    for p in [ROOT / "build", ROOT / f"{NAME}.spec"]:
        if p.is_dir():
            shutil.rmtree(p, ignore_errors=True)
        elif p.exists():
            p.unlink()
    DIST.mkdir(parents=True, exist_ok=True)

    sep = ";" if system == "Windows" else ":"

    cmd = [
        "pyinstaller", "--noconfirm", "--onefile",
        "--name", NAME,
        "--icon", str(ROOT / "src" / "icon.ico"),
        "--add-data", f"{ROOT / 'src' / 'icon.ico'}{sep}bin",
        "--add-data", f"{ROOT / 'src' / 'wgelogo.png'}{sep}bin",
        "--add-data", f"{ROOT / 'src' / 'vmaf_v0.6.1.json'}{sep}bin",
        "--hidden-import", "scenedetect",
        str(ROOT / "src" / "app.py"),
    ]
    cmd.insert(3, "--windowed" if system == "Windows" else "--noconsole")

    # Bundle all of bin/ into the executable
    if BIN.is_dir():
        for f in sorted(BIN.iterdir()):
            if f.is_file() and f.suffix.lower() in (".exe", ".dll", ".so", ".dylib", ".json", ""):
                idx = next(i for i, v in enumerate(cmd) if v == "--hidden-import")
                cmd[idx:idx] = ["--add-data", f"{f}{sep}bin"]

    subprocess.check_call(cmd, cwd=str(ROOT))

    # ---- Assemble platform-specific release archive ----
    exe_name = f"{NAME}.exe" if system == "Windows" else NAME
    arc_name = f"{NAME}.{VER}.{system.lower()}"

    with tempfile.TemporaryDirectory() as _tmp:
        tmp = Path(_tmp)

        # Copy the built binary
        shutil.copy2(DIST / exe_name, tmp / exe_name)

        # Copy FFmpeg bundle
        if BIN.is_dir():
            shutil.copytree(BIN, tmp / "bin", dirs_exist_ok=True)

        # Copy licenses + README
        for item in ["licenses", "README.md"]:
            src = ROOT / item
            if src.is_dir():
                shutil.copytree(src, tmp / item, dirs_exist_ok=True)
            elif src.exists():
                shutil.copy2(src, tmp / item)

        # Create the archive (7z for smallest size — mx=9 is ultra compression)
        archive_path = str(DIST / f"{arc_name}.7z")
        subprocess.check_call(["7z", "a", "-mx=9", archive_path, "."], cwd=str(tmp))

        print(f"Release: {archive_path}")


if __name__ == "__main__":
    main()

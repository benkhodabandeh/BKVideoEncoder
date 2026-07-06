#!/usr/bin/env python3
import platform, shutil, subprocess, sys
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

    exclude = [
        "torch", "torchvision", "torchaudio",
        "onnxruntime", "onnx", "onnxscript",
        "pandas", "pyarrow", "scipy",
        "matplotlib", "av",
        "notebook", "ipython", "jupyter",
        "tensorflow", "keras",
        "transformers", "datasets",
        "sympy", "networkx",
    ]

    cmd = [
        "pyinstaller", "--noconfirm", "--onedir",
        "--name", NAME,
        "--icon", str(ROOT / "src" / "icon.ico"),
        "--add-data", f"{ROOT / 'src' / 'icon.ico'}{sep}bin",
        "--add-data", f"{ROOT / 'src' / 'wgelogo.png'}{sep}bin",
        "--add-data", f"{ROOT / 'src' / 'vmaf_v0.6.1.json'}{sep}bin",
        "--paths", str(ROOT / "src"),
        "--hidden-import", "scenedetect",
        *(f"--exclude-module={m}" for m in exclude),
        str(ROOT / "src" / "app.py"),
    ]
    cmd.insert(3, "--windowed" if system == "Windows" else "--noconsole")

    # Run PyInstaller; onedir creates DIST/NAME/{exe, _internal/}
    subprocess.check_call(cmd, cwd=str(ROOT))

    # ---- Assemble platform-specific release ----
    out_dir = DIST / NAME
    arc_name = f"{NAME}.{VER}.{system.lower()}"

    # Copy FFmpeg bundle alongside the binary
    if BIN.is_dir():
        shutil.copytree(BIN, out_dir / "bin", dirs_exist_ok=True)

    # Copy licenses + README
    for item in ["licenses", "README.md"]:
        src = ROOT / item
        if src.is_dir():
            shutil.copytree(src, out_dir / item, dirs_exist_ok=True)
        elif src.exists():
            shutil.copy2(src, out_dir / item)

    # Create 7z archive of the entire out_dir (includes NAME/ as root)
    archive_path = str(DIST / f"{arc_name}.7z")
    _7z = shutil.which("7z") or shutil.which("7za") or shutil.which("7zz")
    if not _7z:
        _7z = r"C:\Program Files\7-Zip\7z.exe"  # common Windows path
    subprocess.check_call(
        [_7z, "a", "-mx=9", archive_path, out_dir.name],
        cwd=str(DIST),
    )

    print(f"Release: {archive_path}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Download FFmpeg for the current platform.

Windows/Linux: extracts from BtbN FFmpeg-Builds release archive.
macOS:         installs via Homebrew (pre-installed on GitHub runners).
"""

import platform
import shutil
import subprocess
import sys
import urllib.request
import zipfile
import tarfile
from pathlib import Path

BIN = Path(__file__).resolve().parent.parent / "bin"
BIN.mkdir(exist_ok=True)

BTBN = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest"
BUILDS = {
    "Windows": ("ffmpeg-n7.1-latest-win64-gpl-7.1.zip", "zip"),
    "Linux": ("ffmpeg-n7.1-latest-linux64-gpl-7.1.tar.xz", "tar.xz"),
}


def from_btbn(system):
    fname, _ = BUILDS[system]
    url = f"{BTBN}/{fname}"
    archive = BIN.parent / fname
    print(f"Downloading {url} …")
    urllib.request.urlretrieve(url, archive)
    inner = fname.replace(".tar.xz", "").replace(".zip", "")
    print("Extracting …")
    if fname.endswith(".zip"):
        with zipfile.ZipFile(archive) as z:
            z.extractall(path=BIN.parent)
    else:
        with tarfile.open(archive) as t:
            t.extractall(path=BIN.parent)
    src = BIN.parent / inner / "bin"
    if src.is_dir():
        for f in src.iterdir():
            if f.is_file():
                shutil.copy2(f, BIN / f.name)
                print(f"  {f.name}")
    shutil.rmtree(BIN.parent / inner, ignore_errors=True)
    archive.unlink()


def from_brew():
    print("Installing FFmpeg via Homebrew …")
    subprocess.run(["brew", "install", "ffmpeg"], check=True)
    for exe in ("ffmpeg", "ffprobe", "ffplay"):
        src = shutil.which(exe)
        if src:
            shutil.copy2(src, BIN / exe)
            print(f"  {exe}")
    # ffplay not needed by the app, but harmless to include
    # ponytail: skip deleting it — 0.1 MB is not worth the complexity


def main():
    system = platform.system()
    if system in BUILDS:
        from_btbn(system)
    elif system == "Darwin":
        from_brew()
    else:
        print(f"Unsupported platform: {system}", file=sys.stderr)
        sys.exit(1)
    print("Done.")


if __name__ == "__main__":
    main()

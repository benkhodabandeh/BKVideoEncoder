#!/usr/bin/env python3
"""Download FFmpeg from BtbN releases for the current platform.

Called by CI before build.py. Populates bin/ with FFmpeg executables
and shared libraries for the host platform.
"""
import os, platform, shutil, sys, urllib.request, zipfile, tarfile
from pathlib import Path

BIN = Path(__file__).resolve().parent.parent / "bin"
BIN.mkdir(exist_ok=True)

BUILDS = {
    "Windows": ("ffmpeg-n7.1-latest-win64-gpl-7.1.zip",        "zip"),
    "Linux":   ("ffmpeg-n7.1-latest-linux64-gpl-7.1.tar.xz",   "tar.xz"),
    "Darwin":  ("ffmpeg-master-latest-macos64-gpl.tar.xz",      "tar.xz"),
}
BASE = "https://github.com/BtbN/FFmpeg-Builds/releases/download/latest"


def main():
    system = platform.system()
    b = BUILDS.get(system)
    if not b:
        print(f"Unsupported platform: {system}", file=sys.stderr)
        sys.exit(1)

    fname, _fmt = b
    url = f"{BASE}/{fname}"
    archive = BIN.parent / fname

    print(f"Downloading {url} …")
    urllib.request.urlretrieve(url, archive)

    print("Extracting …")
    # Derive the top-level dir name inside the archive
    inner = fname.replace(".tar.xz", "").replace(".zip", "")
    dst = BIN.parent / inner

    if fname.endswith(".zip"):
        with zipfile.ZipFile(archive) as z:
            z.extractall(path=BIN.parent)
    else:
        with tarfile.open(archive) as t:
            t.extractall(path=BIN.parent)

    # Copy everything from the extracted bin/ to our bin/
    src_dir = dst / "bin"
    if src_dir.is_dir():
        for f in src_dir.iterdir():
            if f.is_file():
                shutil.copy2(f, BIN / f.name)
                print(f"  {f.name}")

    # Cleanup
    shutil.rmtree(dst, ignore_errors=True)
    archive.unlink()
    print("Done.")


if __name__ == "__main__":
    main()

# Windows 11 Build Guide

## 1. Install prerequisites

Install:

- Python 3.11 or 3.12 from python.org.
- Git for Windows.
- 7-Zip.
- Visual C++ Redistributable if your FFmpeg build requires it.

## 2. Clone and create a virtual environment

```powershell
git clone https://github.com/benkhodabandeh/BKVideoEncoder.git
cd BKVideoEncoder
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt pyinstaller
```

## 3. Download FFmpeg

```powershell
python scripts/download_ffmpeg.py
```

Confirm these exist:

```powershell
Test-Path .\bin\ffmpeg.exe
Test-Path .\bin\ffprobe.exe
```

## 4. Run from source

```powershell
python src\app.py
```

## 5. Build portable package

```powershell
python build.py
```

## 6. Smoke test

- Open the app.
- Load a small MP4.
- Select one fast preset.
- Add it to The Plan.
- Start development.
- Cancel once to confirm the UI does not freeze.
- Run one full encode.

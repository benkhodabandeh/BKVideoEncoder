param(
    [string]$Python = "py -3.11"
)

$ErrorActionPreference = "Stop"
Write-Host "Creating Windows release build..." -ForegroundColor Cyan

if (!(Test-Path ".venv")) {
    Invoke-Expression "$Python -m venv .venv"
}
. .\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt -r requirements-dev.txt pyinstaller
python scripts\dev_check.py
python scripts\download_ffmpeg.py
python build.py

Write-Host "Build completed. Check dist/." -ForegroundColor Green

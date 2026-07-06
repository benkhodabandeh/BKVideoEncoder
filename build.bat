@ECHO OFF
ECHO.
ECHO --- BKVideoEncoder Build Script ---
ECHO.

SET VENV_DIR=venv

:: --- 1. Cleanup ---
ECHO [1/5] Cleaning up...
IF EXIST *.spec DEL /F /Q *.spec 2>NUL
IF EXIST build RMDIR /S /Q build 2>NUL
IF EXIST dist RMDIR /S /Q dist 2>NUL
ECHO    Done.
ECHO.

:: --- 2. Virtual environment ---
ECHO [2/5] Setting up Python environment...
IF NOT EXIST %VENV_DIR% (
    python -m venv %VENV_DIR%
)
CALL .\%VENV_DIR%\Scripts\python.exe -m pip install -q --upgrade pip
CALL .\%VENV_DIR%\Scripts\python.exe -m pip install -q -r requirements.txt
CALL .\%VENV_DIR%\Scripts\python.exe -m pip install -q pyinstaller
ECHO    Done.
ECHO.

:: --- 3. Build ---
ECHO [3/5] Building...
CALL .\%VENV_DIR%\Scripts\python.exe build.py
ECHO.
ECHO [4/5] Build complete.
ECHO.

:: --- 4. Result ---
IF EXIST "dist\BKVideoEncoder.*" (
    ECHO [5/5] SUCCESS!
    ECHO Release archive: %CD%\dist\
) ELSE (
    ECHO [5/5] FAILED! Check output above.
)
ECHO.
ECHO --- Done ---
PAUSE

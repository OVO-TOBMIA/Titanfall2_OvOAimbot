@echo off
setlocal

REM Check if Python is installed
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python is not installed, installing Python...
    REM You need to provide the path to the Python installer
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
) else (
    echo Python is already installed
)

REM Execute the ovo_aimbot.py script in the current directory
python ovo_aimbot.py
if %errorlevel% neq 0 (
    echo Script execution failed, exiting...
    exit /b %errorlevel%
)

REM Execute the RSPNVPK command
cd vpk_editor
RSPNVPK.exe englishclient_mp_common.bsp.pak000_dir.vpk
if %errorlevel% neq 0 (
    echo RSPNVPK command execution failed, exiting...
    exit /b %errorlevel%
)

REM Move and overwrite files
copy /y englishclient_mp_common.bsp.pak000_dir.vpk ..\vpk\
copy /y client_mp_common.bsp.pak000_228.vpk ..\vpk\

echo All operations completed!
endlocal

@echo off
setlocal

REM 检查Python是否已安装
where python >nul 2>nul
if %errorlevel% neq 0 (
    echo Python未安装，正在安装Python...
    REM 这里需要你提供Python安装包的路径
    start /wait python-installer.exe /quiet InstallAllUsers=1 PrependPath=1
) else (
    echo Python已安装
)

REM 执行当前目录下的ovo_aimbot.py
python ovo_aimbot.py
if %errorlevel% neq 0 (
    echo 脚本执行失败，退出...
    exit /b %errorlevel%
)

REM 复制vpk文件到vpk_editor文件夹内
copy /y vpk\englishclient_mp_common.bsp.pak000_dir.vpk vpk_editor\

REM 执行RSPNVPK命令
cd vpk_editor
RSPNVPK.exe englishclient_mp_common.bsp.pak000_dir.vpk
if %errorlevel% neq 0 (
    echo RSPNVPK命令执行失败，退出...
    exit /b %errorlevel%
)

REM 移动并覆盖文件
copy /y englishclient_mp_common.bsp.pak000_dir.vpk ..\vpk\
copy /y client_mp_common.bsp.pak000_228.vpk ..\vpk\

echo 完成所有操作！
endlocal

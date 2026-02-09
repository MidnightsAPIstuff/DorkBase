@echo off
title DorkBase - [Setup]
setlocal enabledelayedexpansion

for /F "tokens=1,2 delims=#" %%a in ('"prompt #$H#$E# & echo on & for %%b in (1) do rem"') do set "ESC=%%b"
for /f %%a in ('"prompt $H&for %%b in (1) do rem"') do set "BS=%%a"

echo %ESC%[94m[System]%ESC%[0m Starting environment setup...
echo. > .installing

start /b cmd /v:on /c ^"@echo off ^& for /L %%i in (1,0,1) do (if not exist .installing exit) ^& ^<nul set /p "=!ESC![93m|!BS!" ^& ping -n 2 127.0.0.1 ^>nul ^& ^<nul set /p "=!ESC![93m/!BS!" ^& ping -n 2 127.0.0.1 ^>nul ^& ^<nul set /p "=!ESC![93m-!BS!" ^& ping -n 2 127.0.0.1 ^>nul ^& ^<nul set /p "=!ESC![93m^\!BS!" ^& ping -n 2 127.0.0.1 ^>nul^"

echo %ESC%[97mInstalling modules from requirements.txt...%ESC%[0m
python -m pip install -q -r requirements.txt >nul 2>&1

del .installing >nul 2>&1
timeout /t 1 >nul
echo.
echo %ESC%[92m[Success]%ESC%[0m Installation complete.
pause >nul
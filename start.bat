@echo off
title IntelliLearn Web Platform
cd /d "%~dp0"

echo ========================================================
echo   IntelliLearn - CS3613 AI Study Platform
echo   Launching local web server...
echo ========================================================

where python >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    python serve.py
    pause
    exit /b
)

where node >nul 2>&1
if %ERRORLEVEL% EQU 0 (
    npm start
    pause
    exit /b
)

echo Neither Python nor Node.js was found in PATH.
echo You can run any static HTTP server in this directory.
pause


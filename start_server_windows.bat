@echo off
title Zerto Automation Framework Server
echo ===================================================
echo 1. Checking and Installing Prerequisites...
echo ===================================================

:: Run pip install quietly to ensure all dependencies are met
pip install fastapi uvicorn pyvmomi pytest httpx requests pydantic-settings --quiet --upgrade

echo ===================================================
echo 2. Starting Zerto Enterprise Automation Server...
echo ===================================================

:: Navigate to the application root directory
cd /d "C:\Users\likevin\OneDrive - Hewlett Packard Enterprise\Zerto Product\script and API\Webhook2.0"

:: Launch the Uvicorn production listener
uvicorn main:app --host 0.0.0.0 --port 8000

pause
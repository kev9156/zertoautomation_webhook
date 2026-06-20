#!/bin/bash
# Zerto Automation Framework Startup Script

echo "==================================================="
echo "1. Checking and Installing Prerequisites..."
echo "==================================================="

# Run pip install quietly to ensure all dependencies are met
pip install fastapi uvicorn pyvmomi pytest httpx requests pydantic-settings --quiet --upgrade

echo "==================================================="
echo "2. Starting Zerto Enterprise Automation Server..."
echo "==================================================="

# Navigate to the script location
cd "$(dirname "$0")"

# Start Uvicorn bound to all interfaces
uvicorn main:app --host 0.0.0.0 --port 8000
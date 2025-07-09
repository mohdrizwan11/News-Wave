#!/usr/bin/env pwsh
# News Wave Quick Start Script
Write-Host "🌊 Starting News Wave..." -ForegroundColor Cyan

# Set environment variables
$env:FLASK_CONFIG = "development"
$env:FLASK_DEBUG = "True"

# Run the application
& ".\venv\Scripts\python.exe" "app\app.py"

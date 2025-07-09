#!/usr/bin/env python3
"""
WSGI entry point for News Wave application
"""
import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app.app import app

# This is what Gunicorn will look for
application = app

if __name__ == "__main__":
    app.run()

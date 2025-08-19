#!/usr/bin/env python3
"""
WSGI entry point for News Wave application
Compatible with both Gunicorn and Vercel
"""
import os
import sys

# Add the project directory to the Python path
sys.path.insert(0, os.path.dirname(__file__))

# Import the Flask application
from app.app import app

# This is what Gunicorn and Vercel will look for
application = app

if __name__ == "__main__":
    app.run()

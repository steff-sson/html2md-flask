#!/usr/bin/env python3
"""
Application Entry Point
"""

from app import create_app

# App-Instanz für Gunicorn erstellen
app = create_app()

if __name__ == '__main__':
    # Development Server
    app.run(debug=True, host='0.0.0.0', port=5000)
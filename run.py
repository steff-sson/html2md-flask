#!/usr/bin/env python3
# Diese App wurde mit Hilfe von KI erstellt, nach dem Prinzip "human in the loop"
"""
Application Entry Point
"""

import os
from app import create_app

# App-Instanz für Gunicorn erstellen
app = create_app()

if __name__ == '__main__':
    # Development Server
    debug = os.environ.get('FLASK_DEBUG', 'false').lower() == 'true'
    app.run(debug=debug, host='0.0.0.0', port=5000)
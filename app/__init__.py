"""
Flask Application Factory
"""

from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
    
    # Routes registrieren
    from app.routes import init_routes
    init_routes(app)
    
    return app
"""
Flask Application Factory
"""

import os
from flask import Flask, jsonify
from flask_wtf.csrf import CSRFProtect
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from jinja2 import ChoiceLoader, FileSystemLoader
from pathlib import Path

csrf = CSRFProtect()
limiter = Limiter(key_func=get_remote_address)


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max
    app.config['SECRET_KEY'] = os.environ.get('FLASK_SECRET_KEY', os.urandom(24))

    # CSRF aktivieren
    csrf.init_app(app)

    # Rate Limiter aktivieren
    limiter.init_app(app)

    # 429 als JSON statt HTML
    @app.errorhandler(429)
    def ratelimit_handler(e):
        return jsonify({
            "error": "rate_limit_exceeded",
            "message": "Zu viele Anfragen. Bitte warten Sie einen Moment."
        }), 429

    # automation-themes Templates als Jinja2-Pfad registrieren
    themes_base = Path(app.root_path).parent / "node_modules" / "@steff-sson"
    if themes_base.exists():
        app.jinja_loader = ChoiceLoader([
            FileSystemLoader(str(themes_base)),
            app.jinja_loader
        ])

    # Routes registrieren
    from app.routes import init_routes
    init_routes(app)

    return app

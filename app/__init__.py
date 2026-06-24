"""
Flask Application Factory
"""

from flask import Flask
from jinja2 import ChoiceLoader, FileSystemLoader
from pathlib import Path


def create_app():
    app = Flask(__name__)
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

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

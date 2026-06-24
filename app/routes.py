"""
Flask Routes
"""

from flask import render_template, request, jsonify, send_file
from app.scraper import scrape_url_to_markdown
from app import limiter
from io import BytesIO
import re

def init_routes(app):
    
    @app.route('/')
    def index():
        """Hauptseite"""
        return render_template('index.html')
    
    @app.route('/scrape', methods=['POST'])
    @limiter.limit("10 per minute")
    def scrape():
        """API Endpoint für Scraping"""
        data = request.get_json()
        url = data.get('url', '').strip()
        
        # URL validieren
        if not url:
            return jsonify({'error': 'Bitte URL eingeben'}), 400
        
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        # Scrapen
        markdown, error = scrape_url_to_markdown(url)
        
        if error:
            return jsonify({'error': error}), 400
        
        return jsonify({
            'markdown': markdown,
            'url': url
        })
    
    @app.route('/download', methods=['POST'])
    @limiter.limit("10 per minute")
    def download():
        """Download Markdown als .md Datei"""
        data = request.get_json()
        markdown = data.get('markdown', '')
        url = data.get('url', '')
        
        # Filename aus URL generieren
        filename = re.sub(r'[^\w\s-]', '', url.split('//')[-1].replace('/', '-'))
        filename = f"{filename[:50]}.md"
        
        # Als Download senden
        buffer = BytesIO()
        buffer.write(markdown.encode('utf-8'))
        buffer.seek(0)
        
        return send_file(
            buffer,
            as_attachment=True,
            download_name=filename,
            mimetype='text/markdown'
        )
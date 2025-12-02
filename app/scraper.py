"""
Web Scraper Module
Extrahiert Hauptinhalt von URLs als Markdown
"""

import trafilatura
from typing import Optional, Tuple

def scrape_url_to_markdown(url: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Scraped eine URL und gibt Markdown zurück
    
    Args:
        url: Die zu scrapende URL
        
    Returns:
        Tuple[markdown_content, error_message]
    """
    try:
        # HTML laden
        downloaded = trafilatura.fetch_url(url)
        
        if not downloaded:
            return None, "❌ URL konnte nicht geladen werden"
        
        # Zu Markdown konvertieren
        markdown = trafilatura.extract(
            downloaded,
            output_format='markdown',
            include_links=True,
            include_images=True,
            include_formatting=True
        )
        
        if not markdown:
            return None, "⚠️ Kein Hauptinhalt gefunden"
        
        return markdown, None
        
    except Exception as e:
        return None, f"💥 Fehler: {str(e)}"
"""
Web Scraper Module
Extrahiert Hauptinhalt von URLs als Markdown
"""

import trafilatura
import ipaddress
from urllib.parse import urlparse
from typing import Optional, Tuple

BLOCKED_HOSTS = {"localhost", "127.0.0.1", "0.0.0.0", "169.254.169.254"}
BLOCKED_NETWORKS = [
    ipaddress.ip_network("10.0.0.0/8"),
    ipaddress.ip_network("172.16.0.0/12"),
    ipaddress.ip_network("192.168.0.0/16"),
    ipaddress.ip_network("127.0.0.0/8"),
    ipaddress.ip_network("169.254.0.0/16"),
]


def validate_url(url: str) -> Optional[str]:
    """Prüft URL auf erlaubtes Schema und keine internen IPs."""
    parsed = urlparse(url)
    if parsed.scheme not in ("http", "https"):
        return "Nur http/https erlaubt"
    host = parsed.hostname or ""
    if host.lower() in BLOCKED_HOSTS:
        return "Host nicht erlaubt"
    try:
        ip = ipaddress.ip_address(host)
        if any(ip in net for net in BLOCKED_NETWORKS):
            return "Interne IP nicht erlaubt"
    except ValueError:
        pass  # Hostname, kein IP — OK
    return None


def scrape_url_to_markdown(url: str) -> Tuple[str, Optional[str]]:
    """
    Scraped eine URL und gibt Markdown zurück

    Args:
        url: Die zu scrapende URL

    Returns:
        Tuple[markdown_content, error_message]
    """
    # SSRF-Schutz: URL validieren
    error = validate_url(url)
    if error:
        return "", error

    try:
        # HTML laden
        downloaded = trafilatura.fetch_url(url)
        
        if not downloaded:
            return "", "URL konnte nicht geladen werden"
        
        # Zu Markdown konvertieren
        markdown = trafilatura.extract(
            downloaded,
            output_format='markdown',
            include_links=True,
            include_images=True,
            include_formatting=True
        )
        
        if not markdown:
            return "", "Kein Hauptinhalt gefunden"
        
        return markdown, None
        
    except Exception as e:
        return "", f"Fehler: {str(e)}"
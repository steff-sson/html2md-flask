# 🔄 HTML to Markdown

Extrahiere Webseiten-Hauptinhalte als Markdown. Einfach, schnell, selbstgehostet.

## Features

- URL → Markdown-Vorschau → Download
- Nur Hauptinhalt (keine Navigation/Footer)
- Docker-ready mit GitHub Actions

## Quick Start

### Lokal

```bash
git clone https://github.com/DEIN-USERNAME/html2md-flask.git
cd html2md-flask
pipenv install
pipenv run python run.py
```

Öffne: http://localhost:5000

### Docker (VPS)

```bash
cd /home/user/docker
git clone https://github.com/DEIN-USERNAME/html2md-flask.git
cd html2md-flask
docker-compose up -d
```

### Nginx Config

**Für SWAG:**
```bash
cp nginx/html2md-swag.conf.example \
   /pfad/zu/swag/nginx/proxy-confs/html2md.subdomain.conf
docker restart swag
```

**Für Standard Nginx**
```
cp nginx/html2md.conf.example /etc/nginx/sites-available/html2md.conf
# Passe server_name und SSL-Pfade an
nginx -t
systemctl reload nginx
```

## Updates

```bash
docker compose pull && docker compose up -d
```

## Tech Stack

Flask • Trafilatura • Tailwind CSS • Docker • GitHub Actions

## Lizenz

MIT
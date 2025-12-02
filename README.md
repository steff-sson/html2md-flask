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
docker-compose -f docker-compose.prod.yml up -d
```

**SWAG Config:**
```bash
cp nginx/html2md.subdomain.conf.example \
   /pfad/zu/swag/nginx/proxy-confs/html2md.subdomain.conf
docker restart swag
```

## Updates

```bash
cd /home/user/docker/html2md-flask
docker-compose -f docker-compose.prod.yml pull
docker-compose -f docker-compose.prod.yml up -d
```

## Tech Stack

Flask • Trafilatura • Tailwind CSS • Docker • GitHub Actions

## Lizenz

MIT
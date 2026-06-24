# 🔄 HTML to Markdown

Extrahiere Webseiten-Hauptinhalte als Markdown. Einfach, schnell, selbstgehostet.

## Features

- URL → Markdown-Vorschau → Download
- Nur Hauptinhalt (keine Navigation/Footer)
- automation-themes (Tailwind CSS Dark-Mode)
- Docker-ready mit Multi-Stage Build

## Quick Start

### Lokal

```bash
git clone https://github.com/steff-sson/html2md-flask.git
cd html2md-flask
make install
make dev
```

Öffne: http://localhost:5000

### Docker

```bash
docker build -t ghcr.io/steff-sson/html2md-flask:latest .
docker compose up -d
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

## Makefile Targets

| Target | Beschreibung |
|--------|-------------|
| `make install` | venv + npm install |
| `make dev` | Flask Dev-Server (Port 5000) |
| `make css-build` | Tailwind CSS bauen |
| `make css-watch` | Tailwind CSS watch mode |
| `make docker-build` | Docker Image bauen |
| `make docker-up` | Docker Container starten |
| `make docker-down` | Docker Container stoppen |

## Updates

```bash
docker compose pull && docker compose up -d
```

## Tech Stack

Flask • Trafilatura • Tailwind CSS (automation-themes) • Docker • GitHub Actions

## Lizenz

MIT

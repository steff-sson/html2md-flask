# Build stage: Tailwind CSS
FROM node:20-alpine AS build
WORKDIR /build
COPY package*.json ./
RUN npm ci
COPY app/static/css/ ./app/static/css/
COPY app/templates/ ./app/templates/
RUN npx @tailwindcss/cli -i ./app/static/css/style.css -o ./app/static/css/output.css --minify

# Runtime stage
FROM python:3.13-slim
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /app
COPY app/ ./app/
COPY run.py .
COPY requirements.txt .
COPY --from=build /build/app/static/css/output.css ./app/static/css/output.css
RUN python3 -m venv .venv && .venv/bin/pip install --no-cache-dir -r requirements.txt
RUN useradd -m -u 1000 appuser && chown -R appuser:appuser /app
USER appuser
EXPOSE 5000
CMD [".venv/bin/gunicorn", "--bind", "0.0.0.0:5000", "--workers", "2", "--timeout", "120", "run:app"]

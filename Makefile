.PHONY: install dev css-build css-watch docker-build docker-up docker-down clean

install:
	python3 -m venv .venv
	.venv/bin/pip install -r requirements.txt
	npm install

dev:
	.venv/bin/python run.py

css-build:
	npx @tailwindcss/cli -i app/static/css/style.css -o app/static/css/output.css

css-watch:
	npx @tailwindcss/cli -i app/static/css/style.css -o app/static/css/output.css --watch

docker-build:
	docker build -t ghcr.io/steff-sson/html2md-flask:latest .

docker-up:
	docker compose up -d

docker-down:
	docker compose down

clean:
	rm -rf .venv __pycache__ node_modules app/static/css/output.css

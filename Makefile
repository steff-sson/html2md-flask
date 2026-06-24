.PHONY: install dev css-build css-watch clean

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

clean:
	rm -rf .venv __pycache__ node_modules app/static/css/output.css

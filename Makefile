.PHONY: streamlit/start streamlit/stop

format_code:
	poetry run isort .
	poetry run black .

lint:
	poetry run black --check .
	poetry run flake8 --max-line-length=99 --exclude .git,__pycache__,.venv
	poetry run mypy src --allow-untyped-decorators

streamlit/start:
	docker compose up --build -d

streamlit/stop:
	docker compose down
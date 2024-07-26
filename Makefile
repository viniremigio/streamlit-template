.PHONY: streamlit/start streamlit/stop

streamlit/start:
	docker compose up --build -d

streamlit/stop:
	docker compose down
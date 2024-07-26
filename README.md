# Streamlit Template
Template to Streamlit projects. This template embeds [DuckDB](https://duckdb.org/)

## Development
Docker, Docker Compose, and Poetry installation are required. Then run the following commands to develop. 


```shell
poetry lock
poetry install -vvv
source $(poetry env info --path)/bin/activate
```

Also run quality checks with `make format_code` and `make lint`

## How to Run
Execute `make streamlit/start`, then access the app in `http://localhost:8501`. Due to the volumes mounted in the docker-compose.yml file, you are able to change code and refresh the browser.

`make streamlit/stop` kill the container.

## TODO 
- How to deploy the application in the Cloud
- Github Actions

## Dataset
CSV file in the [data](data/) folder was downloaded from this [link](https://www.footballwebpages.co.uk/premier-league/league-table)

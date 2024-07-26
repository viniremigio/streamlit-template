#!/bin/sh

# Init duckdb database
python ./src/database.py

# Run app
streamlit run ./src/main.py --server.port=8501 --server.address=0.0.0.0
echo "Done!"
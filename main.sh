#!/bin/bash

# Move to the script directory
cd "$(dirname "$0")" || exit 1

# Check if running locally or for GitHub Pages
if [[ "$1" == "local" ]]; then
    BASE_PATH="/"
else
    BASE_PATH="/staticsite/"
fi

# Run the Python script with the appropriate base path
python3 src/main.py "$BASE_PATH"

# If running locally, start the local server
if [[ "$1" == "local" ]]; then
    cd docs && python3 -m http.server 8888
fi




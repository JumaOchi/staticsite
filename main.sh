#!/bin/bash

# Move to the script directory
cd "$(dirname "$0")" || exit 1

# Set the basepath (GitHub Pages repo name)
BASE_PATH="/staticsite/"

# Run the Python script with the basepath
python3 src/main.py "$BASE_PATH"

# Serve the site locally (always uses /)
cd public && python3 -m http.server 8888


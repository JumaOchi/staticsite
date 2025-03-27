#!/bin/bash

# Move to the directory where the script is located
cd "$(dirname "$0")" || exit 1


python3 src/main.py
cd public && python3 -m http.server 8888

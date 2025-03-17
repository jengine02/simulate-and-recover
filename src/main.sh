#!/bin/bash

source ../venv/bin/activate

# Navigate to the project root if needed
cd "$(dirname "$0")"

# Execute the main Python script
python3 main.py

# Optional: echo status
echo "Simulation pipeline finished."
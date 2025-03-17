#!/bin/bash

# Optional: Activate virtualenv if needed
# source ../venv/bin/activate

# Navigate to tests directory
cd "$(dirname "$0")"

# Run pytest (assuming you're using pytest)
pytest --maxfail=5 --disable-warnings -v

# Optional: echo status
echo "Test suite completed."
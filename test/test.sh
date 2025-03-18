#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting test suite..."

# Test that the simulation runs without errors
echo "Running simulation for N = 10"
python3 ../src/simulate_recover.py --n_trials 10 --iterations 100 --output ../results/recovery_N10.csv
echo "Simulation for N = 10 passed."

echo "Running simulation for N = 40"
python3 ../src/simulate_recover.py --n_trials 40 --iterations 100 --output ../results/recovery_N40.csv
echo "Simulation for N = 40 passed."

echo "Running simulation for N = 4000"
python3 ../src/simulate_recover.py --n_trials 4000 --iterations 100 --output ../results/recovery_N4000.csv
echo "Simulation for N = 4000 passed."

# Test that the results CSV files exist
echo "Testing if recovery files are generated..."
if [[ ! -f "../results/recovery_N10.csv" ]]; then
  echo "Error: recovery_N10.csv not found!"
  exit 1
fi

if [[ ! -f "../results/recovery_N40.csv" ]]; then
  echo "Error: recovery_N40.csv not found!"
  exit 1
fi

if [[ ! -f "../results/recovery_N4000.csv" ]]; then
  echo "Error: recovery_N4000.csv not found!"
  exit 1
fi

echo "Recovery CSV files exist."

# Test if the recovery plot is generated
echo "Testing if the recovery plot is generated..."
if [[ ! -f "../results/recovery_plots.png" ]]; then
  echo "Error: recovery_plots.png not found!"
  exit 1
fi

echo "Test suite passed."
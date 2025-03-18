# Use of ChatGPT to help write parts of code

#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

echo "Starting EZ diffusion model simulate-and-recover exercise..."

# Create results directory if it doesn't exist
mkdir -p ../results

# Run the simulation script for N = 10, 40, 4000
for N in 10 40 4000
do
    echo "Running 1000 simulations for N = $N..."
    python3 simulate_recover.py --n_trials $N --iterations 1000 --output ../results/recovery_N${N}.csv
done

# Optionally generate plots
echo "Generating recovery plots..."
python3 simulate_recover.py --plot --output ../results/recovery_plots.png

echo "Simulate-and-recover complete. Results saved in results/ directory."
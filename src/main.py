import os
import pandas as pd
from simulate_recover import EZDiffusion

# -- Simulating Data --
def main():
    # Initialize the model
    model = EZDiffusion()

    # Run the simulation
    final_result = model.run_sim_samples(N=[10, 40, 4000], iterations=1000)

    # Convert the final_result to a DataFrame if it is a list
    if isinstance(final_result, list):
        final_result = pd.DataFrame(final_result)

    os.makedirs("results", exist_ok=True)
    final_result.to_csv("results/ez_diffusion_final_results.csv", index=False)

if __name__ == "__main__":
    main()
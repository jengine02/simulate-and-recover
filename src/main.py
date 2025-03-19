import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from simulate_recover import EZDiffusion

# -- Simulating Data --
def main():
    # Initialize the model
    model = EZDiffusion()

    # Run the simulation
    N_values = [10, 40, 4000]
    final_bias, final_sq_error = model.run_sim_samples(N=N_values, iterations=1000)

    # Convert the final_bias and final_sq_error to numpy arrays for easier averaging
    final_bias = [np.array(bias) for bias in final_bias]
    final_sq_error = [np.array(sq_error) for sq_error in final_sq_error]

    # Calculate the average bias and average squared error
    avg_bias = [np.mean(bias, axis=0) for bias in final_bias]
    avg_sq_error = [np.mean(sq_error, axis=0) for sq_error in final_sq_error]

    # Create results directory if it doesn't exist
    os.makedirs("results", exist_ok=True)

    # Define labels for the parameters
    labels = ['v', 'a', 't']

    # Create a figure with subplots for each N value
    fig, axs = plt.subplots(len(N_values), 2, figsize=(10, 4 * len(N_values)))

    # Loop through each N value and generate plots
    for i, N in enumerate(N_values):
        # Reshape the averages to be 2-dimensional
        avg_bias_N = np.array(avg_bias[i]).reshape(-1, 3)
        avg_sq_error_N = np.array(avg_sq_error[i]).reshape(-1, 3)

        # Convert the averages to DataFrames for saving
        avg_bias_df = pd.DataFrame(avg_bias_N, columns=['v', 'a', 't'])
        avg_sq_error_df = pd.DataFrame(avg_sq_error_N, columns=['v', 'a', 't'])

        # Save the DataFrames to CSV files
        avg_bias_df.to_csv(f"results/ez_diffusion_avg_bias_N{N}.csv", index=False)
        avg_sq_error_df.to_csv(f"results/ez_diffusion_avg_sq_error_N{N}.csv", index=False)

        # Plot average bias
        axs[i, 0].bar(labels, avg_bias_df.mean(), color='skyblue')
        axs[i, 0].set_title(f'Average Bias (b) for N={N}')
        axs[i, 0].set_ylabel('Bias Value')
        axs[i, 0].axhline(0, color='gray', linestyle='--')
        axs[i, 0].set_ylim(-3, 1)  # Set y-axis limits for bias plot

        # Plot average squared error
        axs[i, 1].bar(labels, avg_sq_error_df.mean(), color='salmon')
        axs[i, 1].set_title(f'Average Squared Error (b²) for N={N}')
        axs[i, 1].set_ylabel('Squared Error')
        axs[i, 1].axhline(0, color='gray', linestyle='--')
        axs[i, 1].set_ylim(-1, 10)  # Set y-axis limits for squared error plot

    plt.tight_layout()

    # Save the combined plot as an image file
    plot_path = os.path.join("results", "ez_diffusion_combined_plot.png")
    plt.savefig(plot_path)

    # Show the combined plot
    plt.show()

if __name__ == "__main__":
    main()
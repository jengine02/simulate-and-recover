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
    final_bias, final_sq_error = model.run_sim_samples(N=[10, 40, 4000], iterations=1000)

    # Convert the final_bias and final_sq_error to numpy arrays for easier averaging
    final_bias = [np.array(bias) for bias in final_bias]
    final_sq_error = [np.array(sq_error) for sq_error in final_sq_error]

    # Calculate the average bias and average squared error
    avg_bias = [np.mean(bias, axis=0) for bias in final_bias]
    avg_sq_error = [np.mean(sq_error, axis=0) for sq_error in final_sq_error]

    # Reshape the averages to be 2-dimensional
    avg_bias = np.array(avg_bias).reshape(-1, 3)
    avg_sq_error = np.array(avg_sq_error).reshape(-1, 3)

    # Convert the averages to DataFrames for saving
    avg_bias_df = pd.DataFrame(avg_bias, columns=['v', 'a', 't'])
    avg_sq_error_df = pd.DataFrame(avg_sq_error, columns=['v', 'a', 't'])

    os.makedirs("results", exist_ok=True)
    avg_bias_df.to_csv("results/ez_diffusion_avg_bias.csv", index=False)
    avg_sq_error_df.to_csv("results/ez_diffusion_avg_sq_error.csv", index=False)

    # Plot the results
    labels = ['v', 'a', 't']
    fig, axs = plt.subplots(1, 2, figsize=(10, 4))

    # Plot average bias
    axs[0].bar(labels, avg_bias_df.mean(), color='skyblue')
    axs[0].set_title('Average Bias (b)')
    axs[0].set_ylabel('Bias Value')
    axs[0].axhline(0, color='gray', linestyle='--')

    # Plot average squared error
    axs[1].bar(labels, avg_sq_error_df.mean(), color='salmon')
    axs[1].set_title('Average Squared Error (b²)')
    axs[1].set_ylabel('Squared Error')
    axs[1].axhline(0, color='gray', linestyle='--')

    plt.tight_layout()
    
    # Save the plot as an image file
    plot_path = os.path.join("results", "ez_diffusion_plot.png")
    plt.savefig(plot_path)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
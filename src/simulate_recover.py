import numpy as np



class EZDiffusion:
    def __innit__(self):
        N = [10, 40 , 4000]
        iterations = 1000


    # Assign Random Parameters
    def random_parameters(self):
        a = np.random.uniform(.5, 2)
        v = np.random.uniform(.5, 2)
        t = np.random.uniform(.1, .5)

        return a, v, t
    
    # -- Generating 'Predicted' Summary Statistics --
    def generate_ss(self, a, v, t, N, num_samples):
        y = np.exp(-a * v)

        # R Predicted
        Rpred = 1 / (y + 1)

        # M Predicted
        Mpred = t + (a/(2 * v)) * ((1 - y)/(1 + y))

        # V Predicted
        Vpred = (a/(2 * (v**3))) * ((1 - (2 * a * v * y) - (y**2))/((y + 1)**2))

        return Rpred, Mpred, Vpred

    # -- Simulating 'Observed' Summary Statistics --
    def simulate_ss(self, Rpred, Mpred, Vpred, N, num_samples):
        # Use of ChatGPT to help with use of numpy functions
        num_samples = 1

        # Simulate Tobs
        Robs_samples = np.random.binomial(n=N, p=Rpred, size=num_samples)
        print("Robs = ", Robs_samples)

        # Simulate Mobs
        variance = Vpred / N
        std_dev = np.sqrt(variance)
        Mobs_samples = np.random.normal(loc=Mpred, scale=std_dev, size=num_samples)
        print("Mobs = ", Mobs_samples)

        # Simulate Vobs
        alpha = (N - 1) / 2
        beta = (2 * Vpred) / (N - 1)
        Vobs_samples = np.random.gamma(shape=alpha, scale=beta, size=num_samples)
        print("Vobs = ", Vobs_samples)

        return Robs_samples, Mobs_samples, Vobs_samples

    # -- Calculate 'Estimated' Parameters --
    # Debugged using ChatGPT
    def calculate_estimates(self, Robs, Mobs, Vobs):
        eps = 1e-12 # Avoid division by zero or log(0)
        R_obs_clipped = np.clip(Robs, 1e-6, 1 - 1e-6)
        L = np.log((R_obs_clipped) / (1 - R_obs_clipped))

        # Drift Rate
        sgn = np.sign(Robs - 0.5)
        numerator = L * (R_obs_clipped**2 * L - R_obs_clipped * L + R_obs_clipped - 0.5)
        vest_inner = numerator / (Vobs + eps)
        v_est = sgn * np.abs(vest_inner)**(1/4) # Avoid NaNs by forcing non-negative input to root

        # Boundary Separation
        a_est = L / v_est

        # Nondecision Time
        term = (1 - np.exp(-v_est * a_est)) / (1 + np.exp(-v_est * a_est) + eps)
        t_est = Mobs - (a_est / (2 * v_est + eps)) * term

        print(
            "Estimated Drift Rate = ", v_est,
            "\nEstimated Boundary Separation = ", a_est,
            "\nEstimated Nondecision Time = ", t_est
        )
        return v_est, a_est, t_est
    
    # -- Calculate Estimation Bias --
    def calculate_bias(self, v, a, t, v_est, a_est, t_est):
        # Compute bias vector
        b = np.array([v - v_est, a - a_est, t - t_est])

        # Compute squared error (element-wise)
        b_squared = b ** 2

        print("Bias (b):", b)
        print("Squared Error (b^2):", b_squared)

        return b, b_squared
    
    def run_sim_iterations(self, N, iterations):
        bias = []
        sq_error = []

        for i in range(iterations):
            # Step 1: Assign Random Parameters
            a, v, t = self.random_parameters()

            # Step 2: Generate 'Predicted' Summary Statistics
            Rpred, Mpred, Vpred = self.generate_ss(a, v, t, N, num_samples=1)

            # Step 3: Simulate 'Observed' Summary Statistics
            Robs, Mobs, Vobs = self.simulate_ss(Rpred, Mpred, Vpred, N, num_samples=1)

            # Step 4: Calculate 'Estimated' Parameters
            v_est, a_est, t_est = self.calculate_estimates(Robs, Mobs, Vobs)

            #Step 5: Calculate Estimation Bias
            b, b_squared = self.calculate_bias(v, a, t, v_est, a_est, t_est)

            print("Iteration: ", i)
            print("\n")

            bias.append(b)
            sq_error.append(b_squared)
        
        return bias, sq_error
    
    def run_sim_samples(self, N, iterations):
        final_result = []

        for i in N:
            print('Sample Size = ', i)
            result = self.run_sim_iterations(i, iterations)
            final_result.append(result)
        
        return final_result

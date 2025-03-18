import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

# Temporary Testing Parameters
a = 0.5
v = 0.5
t = 0.1
N = 10


# -- Generating 'Predicted' Summary Statistics --
y = np.exp(-a * v)

# R Predicted
Rpred = 1 / (y + 1)

# M Predicted
Mpred = t + (a/(2 * v)) * ((1 - y)/(1 + y))

# V Predicted
Vpred = (a/(2 * (v**3))) * ((1 - (2 * a * v * y) - (y**2))/((y + 1)**2))



# -- Simulating 'Observed' Summary Statistics --
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



# Samples -> Parameters
Robs = Robs_samples
Mobs = Mobs_samples
Vobs = Vobs_samples

# Avoid division by zero or log(0)
eps = 1e-12
R_obs_clipped = np.clip(Robs, 1e-6, 1 - 1e-6)
L = np.log((R_obs_clipped) / (1 - R_obs_clipped))


# -- Calculate 'Estimated' Parameters --
# Debugged using ChatGPT

# Drift Rate
sgn = np.sign(Robs - 0.5)
numerator = L * (R_obs_clipped**2 * L - R_obs_clipped * L + R_obs_clipped - 0.5)
vest_inner = numerator / (Vobs + eps)

# Avoid NaNs by forcing non-negative input to root
v_est = sgn * np.abs(vest_inner)**(1/4)


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



# -- Calculate Estimation Bias --
# Compute bias vector
b = np.array([v - v_est, a - a_est, t - t_est])

# Compute squared error (element-wise)
b_squared = b ** 2

print("Bias (b):", b)
print("Squared Error (b^2):", b_squared)


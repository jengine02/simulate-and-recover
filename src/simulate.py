import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma
import math

# Temporary Testing Parameters
a = 0.5
v = 0.5
t = 0.1
N = 10
num_samples = N


# -- Generating 'Predicted' Summary Statistics --
y = np.exp(-a * v)

# Rpred
Rpred = 1 / (y + 1)
print("Rpred = ", Rpred)

# Mpred
Mpred = t + (a/(2 * v)) * ((1 - y)/(1 + y))
print("Mpred = ", Mpred)

# Vpred
Vpred = (a/(2 * (v**3))) * ((1 - (2 * a * v * y) - (y**2))/((y + 1)**2))
print("Vpred = ", Vpred)



# -- Simulating 'Observed' Summary Statistics --
# Use of ChatGPT to help with use of numpy
# Simulate Tobs
Robs_samples = np.random.binomial(n=N, p=Rpred, size=num_samples)
print("Robs = ", Robs_samples)

# Simulate Mobs
sampling_std = np.sqrt(Vpred / N)
Mobs_samples = np.random.normal(loc=Mpred, scale=sampling_std, size=num_samples)
print("Mobs = ", Mobs_samples)

# Simulate Vobs
alpha = (N - 1) / 2
beta = (2 * Vpred) / (N - 1)
Vobs_samples = np.random.gamma(shape=alpha, scale=beta, size=num_samples)
print("Vobs = ", Vobs_samples)



for i in Robs_samples:
    print("Robs = ", i)
    for i in Mobs_samples:
        print("Mobs = ", i)
        for i in Vobs_samples:
            print("Vobs = ", i)


# -- Calculate 'Estimated' Parameters --
# Temporary Testing Parameters
Robs = .5
Mobs = .5
Vobs = .5

L = math.log(Robs/(1 - Robs))

def DriftRate(Robs, Mobs, Vobs, sgn):
    vest = sgn * (Robs - 0.5) * (((L * (Robs ** 2 - Robs * L + Robs - 0.5))/Vobs) ** 0.25)
    return vest

def BoundarySep(v):
    aest = L / v
    return aest

def NondecisionTime(Mobs, a, v, exp):
    test = Mobs - (a/(2 * v)) * ((1 - exp * (-v * a))/(1 + exp * (-v * a)))
    return test


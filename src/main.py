from testSimulateRecover import *
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gamma

#EZ Diffusion Equations

# Rpred
def predAccuracyRate(y):
    r = 1 / (y + 1)
    return r

# Mpred
def predMeanRT(y, v, a, t):
    m = t + (a/(2 * v)) * ((1 - y)/(1 + y))
    return m

# Vpred
def predVarianceRT(y, v, a, t):
    v = (a/(2 * (v^3))) * ((1 - (2 * a * v * y) - (y^2))/((y + 1)^2))
    return v



# Simulate Tobs
Tobs_samples = np.random.binomial(n=N, p=Rpred, size=num_samples)

# Simulate Mobs
sampling_std = np.sqrt(Vpred / N)
Mobs_samples = np.random.normal(loc=Mpred, scale=sampling_std, size=num_samples)

# Simulate Vobs
alpha = (N - 1) / 2
beta = (2 * Vpred) / (N - 1)
Vobs_samples = np.random.gamma(shape=alpha, scale=beta, size=num_samples)






#Inverse Equations

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





import numpy as np
import matplotlib.pyplot as plt


#Simulating the diffusion process (from lecture)
dt, T, mu, sigma, yO = 0.001, 1, 0.1, 0.5, 0.0
t = np.arange(0, T, dt)
y = np.zeros_like(t) + yO

for i in range(1, len(t)):
    dy = mu * dt + sigma * np.sqrt(dt) * np.random.randn()
    y[i] = y[i-1] + dy





def simulate_ddm(v, a, z, Ter, sigma, dt):
    x = a / 2  # Start at middle point
    t = 0
    trajectory = [x]
    
    while 0 < x < a:
        dx = v * dt + np.random.normal(0, sigma * np.sqrt(dt))
        x += dx
        t += dt
        trajectory.append(x)
    
    # Determine decision and RT
    decision = 1 if x >= a else 0  # 1 = upper boundary, 0 = lower boundary
    RT = Ter + t
    return decision, RT, trajectory




def forwardDriftRate(y):
    driftrate = 1 / (y + 1)
    return driftrate




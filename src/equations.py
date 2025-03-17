#EZ Diffusion Equations

def predAccuracyRate(y):
    r = 1 / (y + 1)
    return r

def predMeanRT(y, v, a, t):
    m = t + (a/(2 * v)) * ((1 - y)/(1 + y))
    return m

def predVarianceRT(y, v, a, t):
    v = (a/(2 * (v^3))) * ((1 - (2 * a * v * y) - (y^2))/((y + 1)^2))
    return v







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





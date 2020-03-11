import numpy as np

# Generalized growth https://www.sciencedirect.com/science/article/pii/S1755436516000037
# TODO: Get this working correctly
def ggrowth(day, r, m):
    # Presume cases(0) = 0
    c0 = 200
    a = c0 ** (1/m) 
    return ((r/m) * day + a) ** m

# Exponential
def egrowth(day, a, x):
    return (a * (np.e ** (day * x)))


# Linear
def lgrowth(day, m):
    return (m * day)
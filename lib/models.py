import numpy as np

# Generalized growth model https://www.sciencedirect.com/science/article/pii/S1755436516000037
# TODO: Get this working correctly
def ggrowth(date, r, m):
    # Presume cases(0) = 0
    c0 = 200
    a = c0 ** (1/m) 
    return ((r/m) * date + a) ** m

# Exponential
def egrowth(date, x):
    return np.e ** x


# TODO: Logistic model
# Generalized growth model https://www.sciencedirect.com/science/article/pii/S1755436516000037
def ggrowth(r, m, t, c0=0):
    a = c0 ** (1/m) 
    return ((r/m) * t + a) ** m
# Generalized growth model https://www.sciencedirect.com/science/article/pii/S1755436516000037
def ggrowth(date, r, m, c0=1):
    a = c0 ** (1/m) 
    return ((r/m) * date + a) ** m
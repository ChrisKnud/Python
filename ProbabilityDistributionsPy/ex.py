import math


def beta_ex(a, b):
    return print("E[X]: ", a / (a + b))

def gamma_ex(shape, scale):
    return print("E[X]: ", shape / scale)

def nb_ex(n, p):
    return print("E[X]: ", n * (1 - p) / p)

def bin_ex(n, p):
    return print("E[X]: ", math.floor((n+1)*p))

import math

# Max
def bin_xmax(n, p):
    return print("X_max: ", math.floor((n + 1) * p))


def nb_xmax(k, p):
    return print("X_max: ", math.floor( ( (1-p) * (k-1)) / p) )

def gamma_max(a, b):
    return print("X_max: ", (a - 1) / b)

def normal_max(a, b):
    return print("X_max: ", a)

def beta_max(a, b):
    return print("X_max", (a-1)/(a+b-2))

def t_max(my, omega, v):
    return print("X_max", my)

def poisson_max(x):
    return print("X_max", math.floor(x))

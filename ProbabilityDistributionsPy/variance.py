# Variance

# Works
def beta_variance(a, b):
    return print("Var: ", (a*b) / ( (a+b)**2 *(a+b+1)))


def bin_variance(n, p):
    return print("Var: ", n * p * (1-p))
# Works
def nb_variance(r, p):
    return print("Var: ", r * (1-p) / (p**2))


def gamma_variance(shape, scale):
    return print("Var: ", shape/(scale**2) )
    #return print("Var: ", (shape * scale**2) / ((shape * scale)**2) )

def normal_variance(n, p):
    return print("Var: ", p**2)

def t_variance(my, omega, v):
    if v > 2:
        return print("Var: ", omega**2 * v/(v-2))
    elif v <= 2:
        return print("Var: infinity")

import numpy as np
import matplotlib.pyplot as plt
import sympy

import numpy as np
from scipy.optimize import minimize

def objective_function_function(X):
    x, y, z = X
    return x**2 + y**2 + z**2

def constraint_function(X):
    x, y, z = X
    return 2 * x - y + z - 3

import autograd.numpy as np
from autograd import grad

def F(L):
    'Augmented Lagrange function'
    x, y, z, _lambda = L
    return objective_function_function([x, y, z]) - _lambda * constraint_function([x, y, z])

# Gradients of the Lagrange function
dfdL = grad(F, 0)

# Find L that returns all zeros in this function.
def obj(L):
    x, y, z, _lambda = L
    dFdx, dFdy, dFdz, dFdlam = dfdL(L)
    return [dFdx, dFdy, dFdz, constraint_function([x, y, z])]

from scipy.optimize import fsolve
x, y, z, _lam = fsolve(obj, [0.0, 0.0, 0.0, 1.0])
print(f'The answer is at {x, y, z}')
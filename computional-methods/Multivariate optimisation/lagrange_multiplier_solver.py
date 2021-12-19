import numpy as np
from scipy.optimize import minimize
def objective(X):
    x, y = X
    return 2*x+2*y
#This is the constraint function that has lambda as a coefficient.
def eq(X):
    x, y = X
    return x*y-1000

import autograd.numpy as np
from autograd import grad

def F(L):
    x, y, _lambda = L
    return objective([x, y]) + _lambda * eq([x, y])

dfdL = grad(F, 0)
# Find L that returns all zeros in this function.
def obj(L):
    x, y, _lambda = L
    dFdx, dFdy, dFdlam = dfdL(L)
    return [dFdx, dFdy, eq([x, y])]

from scipy.optimize import fsolve 

x, y, _lam = fsolve(obj, [1.0, 1.0, 1.0])  #Random initial Variables
print(f'The answer is at {x, y}')
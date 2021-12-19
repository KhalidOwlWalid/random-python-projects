import numpy as np
from scipy.optimize import minimize
from sympy import *
import sympy as sym

# def objective_function(x,y):
#     return (x-5)**2 + (y-8)**2
#     # #This is the constraint function that
#     # has lambda as a coefficient.
# def constraint_function(x,y):
#     return x*y - 5

XX, YY, l = symbols('x y l')
x = 1
y = 1

# Lets name this as P
objective_function = (XX-5)**2 + (YY-8)**2

# Lets name this as A
constraint_function = XX*YY - 5

# Differentiate
dPdx = sym.diff(objective_function, XX)
dPdy = sym.diff(objective_function, YY)
dAdx = sym.diff(constraint_function, XX)
dAdy = sym.diff(constraint_function, YY)

integrate_1 = sym.integrate(objective_function, XX)
integrate_2 = sym.integrate(objective_function, YY)
integrate_3 = sym.integrate(constraint_function, XX)
integrate_4 = sym.integrate(constraint_function, YY)

integrate_1_val = integrate_1.subs([(XX,x), (YY,y)])
dAdx_val = dAdx.subs([(XX,x), (YY,y)])
print(integrate_1_val)
print(dAdx_val)


import numpy as np
import matplotlib.pyplot as plt
import math

#t = 2*pi
# functions that returns dy/dx
# i.e. the equation we want to solve: dy/dx = - y
def model(y,x):
    dydx = -10*y + (1+10)*math.cos(x) - (1-10)*math.sin(x)
    return dydx

# initial conditions
x0 = 0
y0 = 1
# total solution interval
x_final = 6*math.pi
# step size
h = 0.05
# ------------------------------------------------------

# ------------------------------------------------------
# Secant method (a very compact version)
def secant_2(f, a, b, iterations):
    for i in range(iterations):
        c = a - f(a)*(b - a)/(f(b) - f(a))
        if abs(f(c)) < 1e-13:
            return c
        a = b
        b = c
    return c
# ------------------------------------------------------
def analytical_solution(x):
    return np.sin(x) + np.cos(x)
# ------------------------------------------------------
# Euler implicit method

# number of steps
n_step = math.ceil(x_final/h)

# Definition of arrays to store the solution
y_eul = np.zeros(n_step+1)
x_eul = np.zeros(n_step+1)

# Initialize first element of solution arrays 
# with initial condition
y_eul[0] = y0
x_eul[0] = x0 

# Populate the x array
for i in range(n_step):
    x_eul[i+1]  = x_eul[i]  + h

# Apply implicit Euler method n_step times
for i in range(n_step):
    F = lambda y_i_plus_1: y_eul[i] + \
            model(y_i_plus_1,x_eul[i+1])*h - y_i_plus_1
    y_eul[i+1] = secant_2(F, \
            y_eul[i],1.1*y_eul[i]+10**-3,10)
# ------------------------------------------------------

#-------------------------------------------------------
print(y_eul[i+1])
plt.plot(x_eul,y_eul)
plt.plot(x_eul, analytical_solution(x_eul), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.show()
import numpy as np
import sympy as sp
from scipy import integrate
from scipy import optimize
from scipy.misc import derivative
import matplotlib.pyplot as plt

E = 200e9 # Pa
I = 0.0003 # m^4
w_o = 2.5e5 # Nm-1
delta_x = 0.125 # m
L = 3 #m
lower_limit = 0
upper_limit = 3

def theta_integrated_func(x):
    return -0.0083333*E*I*L**5*w_o*x + \
            0.0166666*E*I*L**3*w_o*x**3 - \
            0.0083333*E*I*L*w_o*x**5

def theta_diff_func(x):
    return 0.00833333333333333*E*I*L*w_o*(12.0*L**2*x - 20.0*x**3)

EE, II, LL, ww_0, XX = sp.symbols('E,I,L,w_o,x')

# Define function for the use of sympy
func = (ww_0/120.*EE*II*LL) * (-5.*XX**4 + 6. * LL**2 * XX**2 - LL**4) 

# Integrate using sympy
theta_integrate = sp.integrate(func, XX)
theta_integrate = sp.simplify(theta_integrate)
print(theta_integrate)

# I want to use scipy lol so I define this function
constant = w_o/(120*E*I*L)
theta = lambda x: constant * (-5 * x**4 + 6 * L**2 * x**2 - L**4)

# Define x from lower limit to upper limit with an interval
x = np.arange(lower_limit,upper_limit, delta_x)
theta_data = theta(x)

deflection_data = []

# Calculate the deflection at each point
for i, x_val in enumerate(x):
    deflection , error = integrate.quad(theta,lower_limit,x_val)
    deflection_data.append(deflection)

# Calculate the deflection at a range 
simpson_method = integrate.simpson(theta_data,x)

# Finds the minimum/maximum point of the function
max_deflection = optimize.minimize_scalar(theta_integrated_func)

print(f'The point at which the beam is max is {round(max_deflection.x,4)}')

# ----- QUESTION (B) ------ #

# theta_diff = sp.diff(func, XX)

# moment = E * I * np.diff(theta,upper_limit)


# Plot
fig1, axes1 = plt.subplots(1,2, figsize=(9,3))
axes1[0].plot(x,theta_data)
axes1[1].plot(x,deflection_data)
plt.show()






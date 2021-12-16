import autograd.numpy as np
from autograd import grad
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def objective_function(x,y):
    return (160*x**0.66)*(y**0.33)

#This is the constraint function that
# has lambda as a coefficient.
def constraint_function(x,y):
    return 20*x + 0.15*y - 20000

# Invert the constraint function and make x as variable
def n_x(budget, y):
    return (budget - 0.15 * y)/20

# Make y as the variable 
def n_y(budget, x):
    return (budget - 20 * x)/0.15 

budget = 20000
x_cost = 20
y_cost = 0.15

x_min = 0
x_max = budget/x_cost

y_min = 0
y_max = budget/y_cost

x = np.linspace(x_min, x_max, 100)
y = n_y(budget, x)

plt.figure(figsize=(10,5))
plt.plot(x, y)
plt.xlabel('Number of hours of labour')
plt.ylabel('Number of mass of steel')
plt.title('Possible ways of spending the budget')

from mpl_toolkits.mplot3d import Axes3D
x_axis = np.linspace(x_min, x_max, 100)
y_axis = np.linspace(y_min, y_max, 100)
x_grid, y_grid = np.meshgrid(x_axis, y_axis)

fig = plt.figure()
ax = fig.gca(projection='3d')


ax.plot_surface(x_grid, y_grid, objective_function(x_grid, y_grid))
ax.plot(x,y, linewidth = 5, color = 'r')

ax.set_xlabel('Number of hours bought')
ax.set_ylabel('Number of materials bought')
ax.set_title('Possible ways of spending the budget')


fig, (ax_l, ax_r) = plt.subplots(1, 2, figsize = (15, 5))


im = ax_l.imshow(objective_function(x_grid, y_grid), aspect = 'auto', extent=[x_min, x_max, y_min, y_max])
ax_l.plot(x, y, 'r')
ax_l.set_xlabel('Number of hours of labour')
ax_l.set_ylabel('Number of materials bought')
ax_l.set_title('Possible ways of spending the budget')


# The contours are showing how the intersection looks like
im2 = ax_r.contour(objective_function(x_grid, y_grid), aspect = 'auto', extent=[x_min, x_max, y_min, y_max])
ax_r.plot(x, y, 'r')
ax_l.set_xlabel('Number of hours of labour')
ax_l.set_ylabel('Number of materials bought')
ax_l.set_title('Possible ways of spending the budget')

plt.colorbar(im,ax=ax_l)
plt.colorbar(im2,ax=ax_r)

from sympy import *

# l is lambda
h, s, l = symbols('h s l')

optimized_budget = solve([Eq((320/3) * h ** (-1/3) * s ** (1/3) - 20*l, 0),
                    Eq((160/3) * h ** (2/3) * s ** (-2/3) - 0.15 * l, 0),
                    Eq(20 * h + 0.15 * s - 20000, 0)], [h,s,l], simplify=False)

print(f'Maximum hours for optimization : {optimized_budget[0][0]} \nMaximum amount of materials bought : {optimized_budget[0][1]}')
plt.show()


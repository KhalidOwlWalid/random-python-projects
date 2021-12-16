
import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import solve_ivp

# Define parameters
def ode_functions(x,y_1,y_2,y_3):
    dy1dx = a * (y_2 - y_1)
    dy2dx = sigma * y_1 - y_2 - y_1 * y_3
    dy3dx = -b * y_3 + y_1 * y_2
    return dy1dx, dy2dx, dy3dx

def analytical_solution(x):
    return 3 - 0.998 * np.exp(-1000 * x) - 2.002 * np.exp(-x)

def ode_functions_for_scipy(x,y):
    y_1 = y[0]
    y_2 = y[1]
    y_3 = y[2]
    dy1dx = sigma * (y_2 - y_1)
    dy2dx = rho * y_1 - y_2 - y_1 * y_3
    dy3dx = -b * y_3 + y_1 * y_2
    return dy1dx, dy2dx, dy3dx

def without_solve_ivp():

    # Define the step size
    h = 0.01

    x = np.arange(0, 1 + h, h) # Numerical grid

    # Set the initial condition when x=0
    y0_1 = 4
    y0_2 = 6

    # Explicit Euler Method
    y_1 = np.zeros(len(x))
    y_2 = np.zeros(len(x))

    y_1[0] = y0_1
    y_2[0] = y0_2

    for i in range(0, len(x) - 1):
        # Find next position of y
        gradient1, gradient2 = ode_functions(x,y_1[i],y_2[i])

        y_1[i + 1] = y_1[i] + h*gradient1
        y_2[i + 1] = y_2[i] + h*gradient2

    plt.figure(figsize = (12, 8))
    plt.plot(x, y_1, 'bo--', label='Approximate')
    plt.plot(x, y_2, 'ro--', label='Approximate')
    # plt.plot(x, analytical_solution(x), 'g', label='Exact')
    plt.title('Approximate and Exact Solution \
    for Simple ODE')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()

def with_solve_ivp():
    
    x0 = 0
    x_final = 30
    h = 0.2

    # x = np.arange(x0,x_final,h)
    x = np.linspace(x0,x_final,5000)
    y0_1 = 5
    y0_2 = 5
    y0_3 = 5

    # t_eval = Times at which to store the computed solution, must be sorted and lie within t_span.
    y = solve_ivp(ode_functions_for_scipy, [x0, x_final], [y0_1, y0_2,y0_3], t_eval=x)

    x_data = y.t
    y_1 = y.y[0,:]
    y_2 = y.y[1,:]
    y_3 = y.y[2,:]

    plt.figure(figsize = (12, 8))
    plt.plot(x_data, y_1, 'bo--', label='Approximate')
    plt.plot(x_data, y_2, 'ro--', label='Approximate')
    plt.plot(x_data, y_3, 'go--', label='Approximate')
    # plt.plot(x, analytical_solution(x), 'g', label='Exact')
    plt.title('Approximate and Exact Solution \
    for Simple ODE')
    plt.xlabel('t')
    plt.ylabel('f(t)')
    plt.grid()
    plt.legend(loc='lower right')
    plt.show()


sigma = 10
b = 8/3
rho = 28
with_solve_ivp()
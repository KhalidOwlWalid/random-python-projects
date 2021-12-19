
import matplotlib.pyplot as plt
import numpy as np

# Define parameters
def f(x,y):
    return -1000 * y + 3000 - 2000 * np.exp(-x)

def analytical_solution(x):
    return 3 - 0.998 * np.exp(-1000 * x) - 2.002 * np.exp(-x)

# Define the step size
h = 0.002

x = np.arange(0, 0.3, h) # Numerical grid

# Set the initial condition when x=0
y0 = 0

# Explicit Euler Method
y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h*f(x[i],y[i])

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo--', label='Approximate')
plt.plot(x, analytical_solution(x), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
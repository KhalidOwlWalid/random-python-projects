
import matplotlib.pyplot as plt
import numpy as np

# Define parameters
f = lambda y: y*(1-y) # ODE
h = 0.01 # Step size
x = np.arange(0, 1 + h, h) # Numerical grid
y0 = 0.017862 # Initial Condition

# Explicit Euler Method
y = np.zeros(len(x))
y[0] = y0

for i in range(0, len(x) - 1):
    y[i + 1] = y[i] + h*f(y[i])

plt.figure(figsize = (12, 8))
plt.plot(x, y, 'bo--', label='Approximate')
plt.plot(x, np.exp(x-4)/(np.exp(x-4) + 1), 'g', label='Exact')
plt.title('Approximate and Exact Solution \
for Simple ODE')
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid()
plt.legend(loc='lower right')
plt.show()
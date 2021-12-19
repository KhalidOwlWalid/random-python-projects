import math
from scipy import optimize

def func(x):
    return x**3/3 - x**2/2 - x - 1

def new_x1(x_upper, x_lower):
    return x_upper + (x_lower - x_upper)/phi

def new_x2(x_upper, x_lower):
    return x_lower + (x_upper - x_lower)/phi

def golden_search(func, x_u,x_l,x_1,x_2,epsilon=1e-4):
    
    while ((x_u - x_l) > epsilon):

        if func(x_1) < func(x_2):

            # Update the upper limit value and x_2
            x_u = x_2
            x_2 = x_1

            # Calculate new x_1
            x_1 = new_x1(x_u,x_l)

        elif func(x_1) > func(x_2):

            x_l = x_1
            x_1 = x_2

            x_2 = new_x2(x_u,x_l)

    return x_1

def using_scipy(f):

    maximum = optimize.golden(f, brack=(0,-2), tol = 1e-3)
    print(maximum)

using_scipy(func)

# x_l = 0.7
# x_u = 2
# phi = (1 + math.sqrt(5))/2
# epsilon = 1e-8

# x_1 = x_u + (x_l - x_u)/phi
# x_2 = x_l + (x_u - x_l)/phi

# ans = golden_search(func,x_u,x_l,x_1,x_2)

# print(ans)
        







'biesection method'

import numpy as np
import math 
def f (x):
    return x**3 - x - 1

a = 1 
b = 2


def bisection(a,b):
    for i in range (100):  
    
        c = (a + b)/2
        
        y0 = f(a)
        y1 = f(b)
        y2 = f(c)
        
        if y0*y2 < 0:
            b = c

        elif y0*y2 > 0:
            a = c

        if abs(y2) < 1e-10:
            print('the root is',c)
            return c, i, rel_error
        

    return c,i

root, iteration, rel_error = bisection(a,b)
print(root,iteration, rel_error)
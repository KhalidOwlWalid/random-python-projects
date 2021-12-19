import numpy as np
import math as math

def gsection(ftn, xl, xm, xr, tol = 1e-9):

    gr1 = 1 + (1 + np.sqrt(5))/2
    #
    # successively refine x.l, x.r, and x.m
    fl = ftn(xl)
    fr = ftn(xr)
    fm = ftn(xm)
    while ((xr - xl) > tol):
        if ((xr - xm) > (xm - xl)):
            y = xm + (xr - xm)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xl = xm
                fl = fm
                xm = y
                fm = fy
            else:
                xr = y
                fr = fy
        else:
            y = xm - (xm - xl)/gr1
            fy = ftn(y)
            if (fy >= fm):
                xr = xm
                fr = fm
                xm = y
                fm = fy
            else:
                xl = y
                fl = fy
    print(ftn(xm))
    return(xm)
    
    
xl=0
xm=-2
xr=-4
def ftn(x):
    return 2*math.sin(x)-(x**2/10)
print(gsection(ftn, xl, xm, xr, tol = 1e-9))
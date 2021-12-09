import numpy as np

"""
For dividing polynomials with a factor
"""

# Can be of any nth polynomial
# Lowest to biggest n
# Example: For -3 + 3*x + 4*x**2 
# (-3,3,4)
func_1 = (-120,-46,79,-3,-7,1)

# Give a factor for it to divide with
factor = (3,1)

# Quotient will return all the coefficients left
# If n=6, it will return a 5th order polynomial where
# [a0,a1,a2,a3,a4] Increasing nth order
quotient, remainder = np.polynomial.polynomial.polydiv(func_1,factor)

print(quotient)
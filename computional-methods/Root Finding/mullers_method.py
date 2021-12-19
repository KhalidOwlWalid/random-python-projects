############################
# Demonstration of Muller's Method
# as part of online learning video series on
# YouTube created by Oscar Veliz.
# https://www.youtube.com/OscarVeliz
# @author Oscar Veliz
############################
import cmath

def f(x):
	return x**3 -13*x - 12
xnm2 = 4.5
xnm1 = 5
xn = 5.5
#xnm2 = -2
#xnm1 = -1
#xn = 0
epsilon = 10**-7
i = 0
print("n \t xn \t \t f(xn)")
print("1 \t "+str(xnm2) + " \t \t " + str(f(xnm2)))
print("2 \t " + str(xnm1) + " \t \t "+str(f(xnm1)))
print("3 \t " +str(xn) + " \t \t " +str(f(xn)))

while(abs(f(xn)) > epsilon):
	q = (xn - xnm1)/(xnm1 - xnm2)
	a = q*f(xn) - q*(1+q)*f(xnm1) + q**2*f(xnm2)
	b = (2*q + 1)*f(xn) - (1+q)**2*f(xnm1) + q**2*f(xnm2)
	c = (1 + q)*f(xn)

	#see which x intercept is better
	r = xn - (xn - xnm1)*((2*c)/(b + cmath.sqrt(b**2 - 4*a*c)))
	s = xn - (xn - xnm1)*((2*c)/(b - cmath.sqrt(b**2 - 4*a*c)))

    # Determine which is closer to zero
	if(abs(f(r)) < abs(f(s))):
        # Create a temporary variable to hold our new x
		xplus = r
	else:
		xplus = s

    # Since we might face an imaginary number, we check first 
    # Result is real 
	if xplus.imag == 0j:
		xplus = xplus.real
		print(str(i + 4)+"\t"+str(round(xplus,5))+"\t\t"+str(round(f(xplus),5)))
	else:
		print(str(i + 4)+"\t{:.4f}".format(xplus)+"\t{:.4f}".format(f(xplus)))
    
    # Swap the value
	xnm2 = xnm1
	xnm1 = xn
	xn = xplus

	i = i + 1

print(str(i)+" iterations")

#when root is complex double check complex conjugate
if isinstance(xplus, complex):
	conjugate = complex(xplus.real, -xplus.imag)
	if abs(f(conjugate)) < epsilon:
		print("and \t{:.4f}".format(conjugate)+"\t{:.4f}".format(f(conjugate)))
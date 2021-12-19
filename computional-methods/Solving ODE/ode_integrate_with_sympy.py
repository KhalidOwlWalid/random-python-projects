import sympy as sp
import math

x = 30
f = 60
E = 1.25*10**8
I = 0.05
l = 30

FF, EE, II, LL, ZZ = sp.symbols('ff, EE, II, LL, zz')

d2ydx2 = (FF/(2*EE*II)) * (LL - ZZ)**2

dydx = sp.integrate(d2ydx2, ZZ)
dydx = sp.simplify(dydx)

slope = dydx.subs([(ZZ,x), (EE,E), (FF,f), (II,I), (LL,l)])
print(dydx)
y = sp.integrate(dydx, ZZ)
y = sp.simplify(y)
deflection = y.subs([(ZZ,x), (EE,E), (FF,f), (II,I), (LL,l)])
print(deflection)





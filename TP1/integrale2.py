import numpy as np
import scipy.integrate as spi

#1
def f(x):
    return ((np.sin(x)/x)**2)

a, b = -10, 10

# We get an error because of the x = 0 and the symmetry of the function, given the way scipy.integrate.quad calculates the integral

"""
#Computation of integral using method of rectangles
a, b = -10, 10
N  = 50
S = 0
for i in range(N):
    S += f(a + i*(b-a)/N)
    print("i =", i, "x =", a + i*(b-a)/N, "S =", S)
    S *= (b-a)/N 
"""
# The method of rectangles first produces an error at x=0 and from there the sum is nan as S = ... + nan = nan
     
#2 Modified f
def f_mod(x):
    if x == 0:
        return 1
    else:
        return ((np.sin(x)/x)**2)

def integral(a, b):
    
    return spi.quad(f_mod, a, b, limit = 200)

integr, err = integral(a, b)
print(f"Integral of f from -10 to 10 is {integr:.10f}")

#3
a, b = -100, 200
integr2, err2 = integral(a,b)
print(f"Integral of f from -100 to 200 is {integr2:.10f}")

# The parameter to be fixed was limit in spi.quad to allow more subdivisions when computing the integral

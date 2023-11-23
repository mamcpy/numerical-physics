import numpy as np
import scipy.optimize as spi

def f(tab):
    return tab[0]**2 + tab[1]**2

# The function f1 is f(x,y) = x^2 + y^2

def f2(tab):
    x = tab[0]
    y = tab[1]
    return -0.6 * np.exp(-((x-1)**2 + y**2) / 8) - 0.3 * np.exp(-((x+3)**2 + (y+3)**2) / 2 ) + (x**2 + y**2) / 200

def approxime_gradient(function, xy, d): # f function, xy array 2D vector, d real > 0
    x = xy[0] # (x,y) are the points where gradient is calculated
    y = xy[1]
    #a1 = [x+d, y], a2 = [x-d, y], b1 = [x, y+d], b2 = [x, y-d]
    result = [1 / (2*d) * (f([x+d, y]) - f([x-d, y])), 1 / (2*d) *  (f([x, y+d]) - f([x, y-d]))]
    return result

# We now test approxime_gradient with function f1 and some values of xy

xy = np.zeros(2)

for i in range(3):
    #xy[0,1] = 2*i, 3*i
    xy[0] += 2*i
    xy[1] += 3*i
    d = 1e-3
    print("Gradient of f1 at", xy , "is", approxime_gradient(f, xy, d))

# We obtain a correct result as grad(x^2 + y^2) = (2x, 2y)

def minimize(f, xy0, d = 1e-3, tol_g = 1e-6): # Where xy0 is the initial guess of the minimum
    xy = xy0
    g = approxime_gradient(f, xy, d)
    
    while np.linalg.norm(g)**2 > tol_g**2:
        for n in range(len(xy)):
            xy[n] -= 0.1 * g[n] 
        g = approxime_gradient(f, xy, d)
    return xy

# We now test it over f2
xy0 = [1.2, 3.4]
print(f"The minimum point for f2 starting at {xy0} is", minimize(f2, xy0), "with our minimize function vs",spi.minimize(f2, xy0).x, "with scipy.optimize function")
xy0 = [-3, -3]
print(f"The minimum point for f2 starting at {xy0} is", minimize(f2, xy0), "with our minimize function vs",spi.minimize(f2, xy0).x, "with scipy.optimize function")  

# We get the same result as the scipy.optimize minimize function. The results differ from one initial guess to another because the function f2 does not have a global minimum
    
    
    
    
    
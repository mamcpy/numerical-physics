import numpy as np
from scipy.optimize import minimize
import matplotlib.pyplot as plt

def f3tab(tab):
    x = tab[0]
    y = tab[1]
    return -0.2 * np.exp(-100*((x+4)**2+(y+4)**2)) + (x**2 + y**2)/200

def f3scal(x, y):
        return -0.2 * np.exp(-100*((x+4)**2+(y+4)**2)) + (x**2 + y**2)/200
    
# Find min of f3scal for x,y in [-5, 5] using global opt method

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)
X, Y = np.meshgrid(x,y)

z = f3scal(X,Y)
zmin = z.min()

index = np.unravel_index(z.argmin(), z.shape)
print("The minimum with the global opt method is z=", zmin, "at (x,y)=", (X[index],Y[index]))
print("Using the scipy.optimize method we get z=", minimize(f3tab, [1,1]).fun, "at (x,y)=", minimize(f3tab, [-5,-5]).x)

# The problem is that depending on the initial guess we pass to minimize function we get different minimums and yet the output to see if the process successes is marked as succeed so we assume the function has local and global minimums

fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_surface(X,Y,z,cmap = "viridis" ,edgecolor="none")
plt.show()

# By plotting the function we can see that the global minimum for f3scal(x,y) is at (x,y)= (-3.998998998998999, -3.998998998998999)


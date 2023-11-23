import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

x = np.linspace(-1,1,100)

def function(x):
    f = np.sqrt(1-x**2)
    return f     
    
plt.plot(x, function(x), label = "y = $\sqrt{1 - x^2}$")
plt.xlabel("x")
plt.ylabel("y")
plt.legend(loc = "upper right")

def integral(y, a, b):
    integral = spi.quad(y, a, b )
    return integral

a = -1
b = 1

integr, err = (integral(function, a, b))
print(integr)

"""
L3. Phy Numérique
Question de cours nº1
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import scipy.integrate

def f(t,g,omega = 26, B = 6):
    """
    Function to be used in the exercise
    Params: t real number, g function, omega day [1;31] of birth, B month [1;12] of birth
    Return: B*g(wt)
    """
    return B*g(omega*t)

t = 3
print(f(t, np.sqrt))

a = 2001 # Year of birth

# Student number dozen digit is uneven so we use sin function
def integrand(t):
    """
    Function that returns integrand to be used by scipy.integrate.quad
    Params: t dummy variable to be differentiated in integral
    Return: 
    """
    return f(t,np.sin)

integral, err = scipy.integrate.quad(integrand, 1900, a, limit = 300)
print(integral)




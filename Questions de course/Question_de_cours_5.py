"""
L3. Phy Numérique
Question de cours nº5: Solving DE
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

# Solving diff eq with odeint
def f(X, t, q):
    """
    """   

    x, v = X
    X_dot = [v, -q/x]
    return X_dot

q = 14 #As my prenom is Martinez Camara which has 14 letters
X0 = [2,3] # x0 = 1.1 and v0 = 3 
t = np.linspace(0, 1.1, 100) # [0,T] where T is 1.1

x_sol, v_sol = (scipy.integrate.odeint(f, X0, t, args = (q,)).T) # sol is theta and omega

plt.figure()
plt.plot(t, x_sol, label = "x(t)")
plt.xlabel("t"), plt.ylabel("x")
plt.figure()
plt.plot(x_sol,v_sol)
plt.xlabel("x(t)"), plt.ylabel("v(t)")


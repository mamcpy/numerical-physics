"""
L3. Phy Numérique
TP5- Ej1: Foucault pendulum
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt
%matplotlib qt

def foucault(r, t):
    """
    Function that solves foucault pendulum given coordinates x,y,x_dot,y_dot
    Params: r(x,y) matrix, t day, rest parameters of the eq
    Return: array r_dot = f of x_dot,y_dot,x_dot_dot,y_dot_dot
    """
    g = 9.81 #gravity
    l = 67 #length of fil
    omega = 2*np.pi/24
    wo = np.sqrt(g/l)
    theta = 0.85288
    
    x, y, x_dot, y_dot = r[0], r[1], r[2], r[3]
    f = np.zeros(4)
    f = [x_dot, 
         y_dot, 
         -wo**2*x + 2*omega*np.sin(theta)*y_dot, 
         -wo**2*y -2*omega*np.sin(theta)*x_dot]
    return f

#2
# We get the initial conditions
r0 = [6, 0, 0, 0]
t = np.linspace(0, 60, 1000)

r = scipy.integrate.odeint(foucault, r0, t) #Solves and gets r where in each column we have x, y, x_dot, y_dot

plt.plot(t, r[:,0], label = "x(t)")
plt.plot(t, r[:,1], label ="y(t)")
plt.xlabel("time (t)")
plt.legend(), plt.show()
plt.figure()
plt.plot(r[:,0], r[:,1])
plt.xlabel("x(t)"), plt.ylabel("y(t)")
plt.legend(), plt.show()

print("The value of y just after the first oscillation is 3")



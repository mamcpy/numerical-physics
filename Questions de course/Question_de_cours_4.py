"""
L3. Project Phy Numérique
Question de cours nº4: Monte Carlo
Erasmus: Miguel Ángel Martínez Cámara
"""

import numpy as np
import matplotlib.pyplot as plt
import time # Remove comments on lines of time.time() to check speed 

def f(x,y,z,q):
    """
    Function that checks if the point r(x,y,z) is inside the surface of the eq and returns 1 or 0 depending on whether it is inside or not
    Params: x,y,z coordinates of the point, q parameter for the surface given by the exercise
    Return: 1(0) if inside(outside)
    """
    if x**2 + 1/2*y**2 + 1/q*z**6 <= 1:
        return 1
    else:
        return 0

def volume(q,N):
    #t0 = time.time() 
    Nv = []; Iv = []
    # Instead of setting boundaries of an square that we know contains all the surface given (ex: x,y,z [-2;2]) by our the equation we can optimize it by setting the boundaries as the actual boundaries of the surface by looking at our equation
    x_parall_extremes = [-1,1]
    y_parall_extremes = [-np.sqrt(2), np.sqrt(2)]
    z_parall_extremes = [-np.power(q,1/6), np.power(q,1/6)]
    x = np.random.uniform(x_parall_extremes[0],x_parall_extremes[1],N)
    y = np.random.uniform(y_parall_extremes[0],y_parall_extremes[1],N)
    z = np.random.uniform(z_parall_extremes[0],z_parall_extremes[1],N)
    volume = 2*x_parall_extremes[1]*2*y_parall_extremes[1]*2*z_parall_extremes[1]
    # A question arises regarding on why can't we use a sample of equally spaced points. If we use np.linspace for our enclosing volume with smallest boundaries it arrives at our solution but when we take a bigger volume it fails to take there
    # x = np.linspace(-2,2,N)
    # y = np.linspace(-2,2,N)
    # z = np.linspace(-2,2,N)
    # volume = 4**3

    suma = 0
    for i in range(N):
        # By putting the generation of random number outside of the loop we make the code 2-3 times faster as compared to when they are generated in each iteration of the loop
        # x = np.random.uniform(-2,2)
        # y = np.random.uniform(-2,2)
        # z = np.random.uniform(-2,2)
        suma = suma + f(x[i],y[i],z[i],q)
        if i%10 == 0:
            Nv = np.append(Nv,i)
            Iv = np.append(Iv, volume*suma / float(i + 1))
    #t1 = time.time()
    #print(t1-to)
    return Nv, Iv

q = 14 # As my surname is Martinez Camara and is composed of 14 characters
N = 10**6
Nv, Iv = volume(q,N)
plt.plot(Nv, Iv)
plt.xlabel("Number of points"), plt.ylabel("Volume")
plt.title("Approximation of volume enclosed by surface using MC method")
plt.ticklabel_format(style = "plain")
plt.show()
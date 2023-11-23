"""
L3. Phy Numérique
TP5- Ej2: Linear systems of DE
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import scipy.integrate
import matplotlib.pyplot as plt

def func(r, t, M):
    return M@r

def diag(matrix):
    """
    Receives matrix and returns tab_eigenvalues, tab_eigenvectors
    """
    return np.linalg.eig(matrix)

def matrix_creator(coefs): # Creates matrix from input of coeficients
    a, b, c, d = coefs[0], coefs[1], coefs[2], coefs[3]
    return np.array([[a,b],[c,d]])

N = 8 #number of different initial conditions
t = np.linspace(0, 5, 100)
choice_matrix_elements = np.array([[1,2,3,4],[1,-1,1,2],[-1,1,1,-3],[0,1,-1,0]])

for i in range(len(choice_matrix_elements)):
    M = matrix_creator(choice_matrix_elements[i,:])
    print("matrice is ", M) # To check that we are getting the matrix we expect
    tab_eigenvalues, tab_eigenvectors = diag(M)
    print(f"For matrix composed by ij elements {choice_matrix_elements[i,:]} we get")
    print("Eigenvalues:", tab_eigenvalues)
    print("Eigenvectors:", tab_eigenvectors)
    print("------------------")
    plt.figure() # For each choice_matrix one figure and for each figure N x and y plots with diff initial condition
    for j in range(N):
        ro_xy = np.random.uniform(-3,3,2) # Random initial conditions between 0 and 3
        ro = func(ro_xy, t, M) # Here we have array with xo,yo,xo_dot,yo_dot
        x, y = (scipy.integrate.odeint(func, ro, t,(M,)).T)
    
        plt.plot(t, x, alpha = 0.6, color = "blue")
        plt.plot(t, y, alpha = 0.6, color = "orange")
        plt.xlabel("time (t)")
        plt.title(f"Trajectories for different (xo,yo) with coefs of M {choice_matrix_elements[i,:]}")
    plt.figure()
    
    for j in range(N):
        ro_xy = np.random.uniform(-3,3,2) # Random initial conditions between 0 and 3
        ro = func(ro_xy, t, M) # Here we have array with xo,yo,xo_dot,yo_dot
        x, y = (scipy.integrate.odeint(func, ro, t,(M,)).T)
        plt.title(f"Parametric plot for different (xo,yo) with coefs of M {choice_matrix_elements[i,:]}")
        plt.plot(x,y)
    
    
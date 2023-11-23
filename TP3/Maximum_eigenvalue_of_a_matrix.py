"""
L3. Project Phy Numérique
TD3 - Ej1: Computation of maximum eigenvalue of a matrix
Erasmus: Miguel Ángel Martínez Cámara
"""

import numpy as np

M = np.array([[1,0,4],[-2,3,6],[0,0,5]])

def next(matrix, x_vector):
    """
    Function that returns a vector with direction Mx but unitary norm
    Params: np 2D matrix, np 1D vector
    Return: vector
    """    
    v = matrix @ x_vector
    return v/np.linalg.norm(v)

def iter(matrix, eps = 10**-5):
    """
    F that iterates over next function until it finds the best approximation for eigenvector of highest absolute value eigenvalue of M, for the first x_prec it takes a random vector 
    """
    x_prec = np.array([np.random.uniform(-1,1),np.random.uniform(-1,1),np.random.uniform(-1,1)])
    x_vector = next(M, x_prec)
    x_vector2 = x_vector
    
    while np.linalg.norm(x_vector2 - x_prec) > eps:
        x_prec = x_vector2 
        x_vector2 = next(matrix, x_vector2)
        
    return x_vector2

def valvec(matrix, x_eigenvector):
    eigenvalues = M@x_eigenvector / x_eigenvector
    return eigenvalues

print(f"The biggest eigenvalue of M in absolute value is {round(valvec(M,iter(M))[0])} of the eigenvector {iter(M)}")

# We test it for M2

M2 = np.array([[1,0,4],[-2,3,2],[0,0,5]])
print(f"The biggest eigenvalue of M2 in absolute value is {round(valvec(M2,iter(M2))[0])} of the eigenvector {iter(M2)}")
print(np.linalg.eig(M2))

M3 = [[-3,0,4],[-6,3,2],[0,0,1]]
print(f"The biggest eigenvalue of M3 in absolute value is {round(valvec(M3,iter(M3))[0])} of the eigenvector {iter(M3)}")
print(np.linalg.eig(M3))
# For M3 there is an error in our algorithm 
# The error comes that as there are two eigenvalues of the matrix which have same value but different sign (+3 and -3) our algorithm fails to exit a loop when executed. We realised it because if for M we change first value for -5 our program doesn't compute the first part


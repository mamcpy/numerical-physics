""" 
L3. Project Phy Numérique 
TD2 - Ej1: Calculus with matrix
Erasmus: Miguel Ángel Martínez Cámara
"""

import numpy as np

A = np.array([[2, -2, -3], [-2, -1, -3], [6, 4, 4]])
print(A.shape)
print(A)
L0 = A[0,:]
print(L0)
C2 = A[:,2]
print(C2)
C2c = C2.reshape((3,1))
print(C2c)
# print(np.matmul(C2c,L0)) donne error
print(L0@C2c)
(np.matmul(C2c,C2c.T))

a = np.linalg.norm(L0)
b = np.linalg.norm(C2)

V = np.cross(L0,C2)
Vnorm = np.linalg.norm(V)
print(V)
                                                                                     
theta2 = np.arccos(np.dot(L0,C2)/(a*b))

print(round((theta2*180/(2*np.pi)),2))
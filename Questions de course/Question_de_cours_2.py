"""
L3 Project Phy Numérique 
Question de cours nº2
Erasmus Student: Miguel Ángel Martínez Cámara
"""

import numpy as np

du = 71 #Two last digits of student number: 22206671
m = 6 #Number of the month of birth

vect1 = np.array([[np.cos(np.pi/(1+du))], [np.sin(np.pi/(1+du))]])
vect2 = np.array([[-np.sin(np.pi/(1+du))], [np.cos(np.pi/(1+du))]])

A = np.hstack((vect1,vect2))
B = m * np.array([[0,1],[1,0]])
C = B @ A
row_vect = C[0,:].reshape(2,1)

print("The trace of A is =",np.trace(A))
print("The determinant of B is =",np.linalg.det(B)) # -1
print("The row vector composed by the two elements of the first row of C is", row_vect)
print("The product between C and this vector is", C @ row_vect)


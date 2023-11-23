""" 
L3. Project Phy Numérique 
TD2 - Ej2: Solving a linear system
Erasmus: Miguel Ángel Martínez Cámara
"""

import numpy as np

A = np.array([[8,3,-2], [-4,7,5], [3,4,-12]])
b = np.array([9, 15, 35])

det = np.linalg.det(A) 
# There is only one solution cause the determinant is not zero

sol1 = np.linalg.solve(A,b)

# We check the solution by: Ax = b, A_inv*Ax =A_inv and we arrive to  x = A_inv*b
A_inverse = np.linalg.inv(A) 
# We can check if is the inverse
check = A_inverse@A
sol2 = A_inverse@b
print(sol1, sol2)

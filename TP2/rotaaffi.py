"""
L3. Project Phy Numérique
TD2 - Ej3: Rotation, orthonormal affinity
Erasmus: Miguel Ángel Martínez Cámara
"""

import numpy as np
import matplotlib.pyplot as plt

alpha = np.pi/4
M1 = np.array([[np.cos(alpha), -np.sin(alpha)],[np.sin(alpha), np.cos(alpha)]])

#2
square = np.array([[0,1,1,0,0],[0,0,1,1,0]])
square_after = np.zeros(shape = square.shape) 
square_after = M1 @ square

""" We avoid doing a loop with the above line
for i in range(4):
    square_after[:,i] = M1 @ square[:,i]
"""  
plt.figure()
plt.plot(square[0,:], square[1,:], '-o', label = "Before transformation")
plt.plot(square_after[0,:], square_after[1,:], '-o', label = "After transformation")
plt.title("Rotation of square by $\dfrac{\pi}{4}$ rad")
plt.axis('scaled')
plt.legend(bbox_to_anchor = (1,1)), plt.show()
   
#3
M2 = np.identity(2)
ky = 2
M2[1,1] = ky

square_after = M2 @ square
plt.figure()
plt.plot(square[0,:], square[1,:], '-o', alpha = 1, label = "Before transformation")
plt.plot(square_after[0,:], square_after[1,:], '-o', alpha = 0.6, markersize = 2, label = "After transformation")
plt.xlabel('x'), plt.ylabel('y')
plt.axis('scaled')
plt.title(f"Orthonormal affinity with kx = 1 and ky = {ky}")
plt.legend(bbox_to_anchor = (1 , 1)), plt.show()    

#4

M3 = M1@M2
square_after = M3 @ square
plt.figure()
plt.plot(square[0,:], square[1,:], '-o', alpha = 1, label = "Before transformation")
plt.plot(square_after[0,:], square_after[1,:], '-o', alpha = 0.6, markersize = 2, label = "After transformation")
plt.xlabel('x'), plt.ylabel('y')
plt.axis('scaled')
plt.title(f"Orthonormal affinity with kx = 1 and ky = {ky}")
plt.legend(bbox_to_anchor = (1 , 1)), plt.show()    

# We don't obtain the same if we do the rotation first as matrix product is in general not commutative

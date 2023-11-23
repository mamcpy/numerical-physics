"""
L3. Phy Numérique
TP6 - Ej1: Leapfrog Method to solve PDE (partialdifeq)
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import matplotlib.pyplot as plt

T = 2
L = 3
ax, bx = 0, L 
ay, by= 0, T

def leapfrog(Nx,Ny,ax,bx,ay,by):
    c = 3
    A = 2

    dx = (bx-ax)/float(Nx)
    dy = (by-ay)/float(Ny)
    y = np.zeros((Nx,Ny))
    fact = c**2*(dy**2/dx**2)
    # For i,  j = 0 we do first by ourselves
    i = 0 
    for it in range(Nx):
        y[i,0] = A * np.sin(np.pi * it*dx / L)
        y[i,1] = (1-fact)*y[i,0] 
        + 1/2*fact*(y[i+1,0] +y[i-1,0])
        # for next i, j = 1,2,...
        for i in range(1, Nx-1):
            for j in range(Ny-1):
                y[i,j+1] = (1-fact)*y[i,j]
                + 1/2 *fact*(y[i+1,j] +y[i-1,j])
    return y

Nx=40;Ny=40
z=leapfrog(Nx,Ny,ax,bx,ay,by)
x=np.linspace(ax,bx,Nx)
y=np.linspace(ay,by,Ny)
X, Y = np.meshgrid(x, y)
Z = z.reshape(Nx, Ny)

CS = plt.contour(X, Y, z)
plt.clabel(CS, inline=1, fontsize=10,fmt='%s')
plt.xlabel('x')
plt.ylabel('t')
# plt.savefig('chambre.png')
plt.show()

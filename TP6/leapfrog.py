"""
L3. Phy Numérique
TP6 - Ej1: Leapfrog Method to solve PDE (partialdifeq)
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import matplotlib.pyplot as plt

def initial_cond(xi,A,L):    
    return A * np.sin(np.pi *xi*dx / L)

L, T = 20, 10
c = 0.5 #propagation speed
Nt, Nx = 1000, 1000
x = np.linspace(0, L, Nx + 1)
t = np.linspace(0, T, Nt + 1)
dx = L/Nx
dt = T/Nt
A = 2
C = c*dt/dx
un = np.zeros(Nx+1)
u = np.zeros((Nx+1,Nt+1))
unminus1 = np.zeros(len(u))

# un denotes for when n=n and not n+1 or n-1
# We have u(i,0) from the initial condition
for i in range(0, Nx+1):
    un[i] = initial_cond(x[i], A, L)
    
# and get u(i,n = 1) which we know from initial condition 
for i in range(0, Nx):
    u[i] = un[i] - 1/2*C**2*(un[i-1] - 2*un[i] + un[i-1])

u[0], u[Nx] = 0, 0
unminus1[:], un[:] = un, u[:,0]

# Now we do the actual loop
for n in range(1, Nt):
    for i in range(1, Nx):
        u[i, n] = -unminus1[i] + 2*un[i] + C**2*(un[i+1] - 2*un[i] + un[i-1])
    u[0,n], u[Nx,n] = 0, 0
    unminus1[:], un[:] = un, u[:,n]

X, T = np.meshgrid(x, t)
CS = plt.contour(X, T, u) #, levels=range()))
# plt.clabel(CS, inline=1, fontsize=10,fmt='%s')
plt.xlabel('x')
plt.ylabel('t')
plt.show()

X, T = np.meshgrid(x, t)
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, T, u, cmap='coolwarm', linewidth=0)
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('u(x,t)')
plt.show()

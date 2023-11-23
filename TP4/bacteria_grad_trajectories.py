"""
TD4 - EJ3 Chimiotactisme
Concepts: gradient descent
Bacteria that moves with constant v orienting following >0 grad(of glucose) but randomly rotates and rotation is different if bacteria moving in >0 grad(glucose) or in <0 grad(glucose)
"""
import numpy as np
import matplotlib.pyplot as plt
#matplotlib qt#
from scipy.optimize import minimize

def f_concentration(xy, Co=1000, C1=500):
    """
    Function of the concentration of glucose
    Imputs: -x,y coordenates
    Returns: calculated concentration of glucose for point (x,y)
    """
    x = xy[0]
    y = xy[1]
    return Co*np.exp(-((x-2)**2 + (y-2)**2)*1/2) + C1*np.exp(-((x-6)**2 + (y-6)**2)*1/4)

def prob_change_direction(xy, v, grad, p1 = 0.1, p2 = 0.2):
    """
    Probability of bacteria changing direction (depends on vect of velocity * vect of gradient)
    Imputs: vector v velocity
    Return: probability of changing direction for the given velocity        
    """
    return p1 + p2/2 * (1 -np.tanh(np.dot(v,gradient(f_concentration, xy))/np.linalg.norm(v)))           #velocity vector * function that calculates grad of C)/modul of v)

def gradient(f, xy, d = 1e-3):
    """
    Calculation of gradient 
    Imputs: f is function to calculate grad, xy 2D array of coordenates to calculate grad, d
    Return: grad calculated, # I would like to also return the xy for the new point
    """
    x = xy[0] # (x,y) are the points where gradient is calculated
    y = xy[1]
    return [1 / (2*d) * (f([x+d, y]) - f([x-d, y])), 1 / (2*d) *  (f([x, y+d]) - f([x, y-d]))]                    
               
#1 Simulate displacement of several bacteria starting from random initial position x,y [0;10]
# Remind that v is fixed and is its direction what changes with prob_change_direction which will be computed after each displacement                                    

dt = 1 # Tamaño de paso  v = de/dt
v_norm = 0.01 # speed
N = 20 # Numbers of iterations

# Random initial position and velocity
xy = np.random.uniform(0,10,size=2)
a = np.random.uniform(0,1,size=2)
v0 = v_norm * a/np.linalg.norm(a) # To get v0 vector with norm = v

# Make for loop until it finds the minimum

# We calculate initial grad 1st
grad = gradient(f_concentration, xy)
v_direction = grad
#prob = prob_change_direction(xy0, v0, grad)

xy_trajectory = np.zeros((N+1,3)) 
xy_trajectory[0,0] = xy[0] 
xy_trajectory[0,1] = xy[1]
xy_trajectory[0,2] = f_concentration(xy)

for j in range(1,N+1): # For starts at 1 cause of calculate 1st v_direction later (if it didn't j-1 would be -1 and not 0)
    for i in range(len(xy)):
        xy[i] += (dt*v_norm) * grad[i]  # Tamaño de paso igual es 0.1 y no d 
    grad = gradient(f_concentration, xy)  
    v_direction = xy - [xy_trajectory[j-1,0], xy_trajectory[j-1,1]]
    prob = prob_change_direction(xy, v_direction, grad) 
    xy_trajectory[j,0] = xy[0] # Array of N elements where each element has the coordinates of each displacement
    xy_trajectory[j,1] = xy[1] 
    xy_trajectory[j,2] = f_concentration(xy)
    
    if np.random.uniform(0,1) < prob_change_direction(xy, v_direction, grad): # Change in direction when random number between 0 and 1 is < prob of change direction (makes sense if you think about prob change direction being 1)
        alpha = np.random.uniform(0,2*np.pi)    
        v_direction = v_direction*[np.cos(alpha), np.sin(alpha)]
    grad = gradient(f_concentration, xy)

X,Y = np.meshgrid(np.linspace(0,10,1000),np.linspace(0,10,1000))
xy_glucose = [X,Y]
# Plot of the glucose function
fig = plt.figure()
ax = plt.axes(projection = "3d")
ax.plot_surface(X,Y, f_concentration(xy_glucose), cmap = "viridis", edgecolor = "none", alpha = 0.4)
#ax = plt.axes(projection = "3d")
ax.plot(xy_trajectory[:,0],xy_trajectory[:,1],xy_trajectory[:,2], '-o')
plt.show()
# - bc we want to minimize
#c = minimize(-f_concentration,[0,0]) # initial guess is 0,0



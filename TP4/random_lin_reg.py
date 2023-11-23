import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress


#1
N = [10**3, 10**4, 10**5]
k = [1, 2, 3]


def aver_x(random_tab, k, i):
    return np.mean(random_tab**k), 1/(k+1) 
        
x_averageA = np.zeros((3,3)) #Each row of same N and in each column k1, k2, k3
x_averageB = np.zeros((3,3))

for j in range(len(N)):
    random_tab = (np.random.random(N[j]))
    for i in range(len(k)):
        x_averageA[j,i], x_averageB[j,i] = aver_x(random_tab, k[i], i)
        
# As we know both expressions we can O(1/sqrt(N))
dif = abs(x_averageB - x_averageA)

x = np.linspace(10**3.1, 10**5, 100)    
y = 1/np.sqrt(x)

#2 Test to verify uncorrelation between a number x(i) and the next x(i+1)
x_averageB2 = 1/4*np.ones(3) # Now x_averageB=1/4
x_averageA2 = np.zeros(3)

for j in range(3):
    random_tab2 = (np.random.random(N[j]))
    x_averageA2[j] = 1/(N[j]-1)*np.sum(random_tab2[:-1]*random_tab2[1:])

dif2 = abs(x_averageA2 - x_averageB2)

for i in range(len(k)):
    plt.plot(N, dif[:,i], label = f"T.1 (k = {k[i]})", alpha = 0.7)
plt.plot(N, dif2, label = "Test 2", alpha = 0.7)
plt.plot(x,y, label = r'Curve = $\dfrac{1}{\sqrt{x}}$')
plt.xlabel("N"), plt.ylabel("Dif")
plt.legend(), plt.show()    

# Also plot it with log scale and log(y) for 1st test to appreciate the line

# To get the y-intersect
a = linregress(np.log(N), np.log(dif2)).slope
plt.plot((N), (dif2), label = f"slope = {a:.2f}")
plt.loglog() # As we just took 3 points for our plot sometimes it fails to produce the expected result but many others we can see a 
plt.title("LogLog plot for Test 2 , expected slope = -1/2")
plt.legend(), plt.show()

# 3  & 4 are done in the same way
    
    
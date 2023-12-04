"""
L3. Phy Numérique
Question de cours nº3:
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import matplotlib.pyplot as plt

# Important: We asume there is a mistake in the formulation of the exercise as it says Uo = (0,-l,l,0,0) of 5 components but it has to be of 4 components to be able to perform the operation so we take the first 4th components
c = 6 #Digit of cents of student number: 22206671
m = 6 #Month of birth

def f(t):
    """
    Function that returns [0] component
    Params:
    Return:
    """
    M = np.array([[0,1,0,0],[0,0,1,0],[0,0,0,1],[-16*m**2*(1/2+c)**2*np.pi**4 , 0, -4*(m**2+(1/2+c)**2)*np.pi**2, 0]])
    tab_eigenvalues, P = np.linalg.eig(M)
    tab_diagonal = np.identity(4, dtype = complex)
    for i in range(len(M)): #tab_diagonal is a diagonal matrix which elements are the eigenvalues of M
        tab_diagonal[i,i] = tab_eigenvalues[i]
    l = 13 #Prenom Miguel Angel, M is in position 13
    Uo = np.array([0,-l,l,0]) 
    
    vect = P @ np.exp(t*tab_diagonal) @ np.linalg.inv(P) @ Uo
    return vect[0]

ttab = np.arange(0, 10, 0.01)
xtab = np.zeros(len(ttab), dtype = complex)

for i in range(len(ttab)):
    xtab[i] = f(ttab[i])
    
x = np.arange(0, 100, 0.1)
y = abs(np.fft.fft(xtab)) #Absolute value of FT coefs of xtab 

plt.plot(x, y, '-')
plt.xlabel("N"), plt.ylabel("Modul of FT coeficients")
print("Peaks are at N = 6, 6.5, 93.5 and 94") # As for M there are 4 eigenvalues of which 2 pairs have same real part but opposed imaginary part






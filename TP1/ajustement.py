import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

import scipy.optimize 

# with open('./donnees_chute_libre.csv','r') as data:
# It is easier to use pandas library to extract and manipulate the data

dataread = pd.read_csv('./donnees_chute_libre.csv')
data = [dataread.iloc[:,0].values, dataread.iloc[:,1].values]

t = data[0]
z = data[1]

def z_function(t, to, zo, g):
    return zo - 1/2*g*(t-to)**2

to = 10
std_z = 5

# We have to adjust our function to experimental data
# We need to estimate zo and g of the planet

params, cov = scipy.optimize.curve_fit(z_function, t, z, sigma = np.ones_like(z)*5, absolute_sigma = True)

z_fit = z_function(t, params[0], params[1], params[2])

std = np.sqrt(np.diag(cov))
print("The uncertainties are err_to =",std[0], "err_zo =",std[1], "err_g =",std[2])

plt.errorbar(data[0], data[1], yerr=5, xerr = 1e-6, fmt = 'o', label = "Data")
plt.plot(t, z_function(t, 10, z.max(), 9.81), label = "Guess fit", alpha = 0.8)
plt.plot(t, z_fit, label = "Fit", alpha = 0.8)
plt.xlabel("t (s)")
plt.ylabel("z (m)")
plt.legend(); plt.show()
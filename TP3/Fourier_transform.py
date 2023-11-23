"""
L3. Project Phy Numérique
TD3 - Ej2: Fourier Transform
Erasmus: Miguel Ángel Martínez Cámara
"""

import numpy as np
import matplotlib.pyplot as plt

# Extract and store data from txt

xtab = np.loadtxt("pos_etoile_2ans.txt")
delta_t = 0.01
ttab = np.arange(0, delta_t*(xtab.shape[0]), delta_t)

plt.plot(ttab, xtab)
plt.xlabel("t (years)"), plt.ylabel("x (m)")
# plt.ticklabel_format(style='plain')
plt.show()

# Uncertainty in frec from FT 
# deltaf*deltat = 1

t_un = 2
F_un = 1 / t_un
print("f_un =", F_un, "years^-1")

# FT

ft_xtab = np.fft.fft(xtab)
frec = 1 / (ttab[1] - ttab[0])
f = np.arange(0, 1, 1/len(ttab)) * frec
plt.plot(f, abs(ft_xtab))
plt.xlabel("frecuency (years$^{-1}$)")
plt.figure()
plt.plot(f, abs(ft_xtab))
plt.xlabel("frecuency (years$^{-1}$)")
plt.xlim(0,8)

print("The max of frec is about 2.7 years ^-1")
# Which is, taking into acc the calcultaed uncertainty, involving the precise value of frec max
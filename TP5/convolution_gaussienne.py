import numpy as np
import math
# importation des librairies
import sys
from PIL import Image

import imageio
from matplotlib.pyplot import *
import matplotlib.pyplot as plt

def convolution2D(X,H,moitie):
    s = X.shape
    py = int((H.shape[0]-1)/2)
    px = int((H.shape[1]-1)/2)
    #print(py,px,s)
    Y = X.copy()
    if moitie:
        imax = int(s[1]/2)
        #print("imax,True",imax)
    else:
        imax = int(s[1]-px)
        #print("imax,false",imax)
    for i in range(px,imax):
        #print("px, imax", px, imax)
        for j in range(py,s[0]-py):
            somme = 0.0
            for k in range(-px,px+1):
                for l in range(-py,py+1):
                    somme += X[j+l][i+k]*H[l+py][k+px]
            Y[j][i] = somme
    return Y



def filtreGaussien(P):
    epsilon = 0.05
    sigma = P*1.0/math.sqrt(-2*math.log(epsilon))
    h = np.zeros((2*P+1,2*P+1))
    som = 0
    for m in range(-P,P+1):
        for n in range(-P,P+1):
            h[m+P][n+P] = math.exp(-(n*n+m*m)/(2*sigma*sigma))
            som += h[m+P][n+P]
    h = h/som
    return h



img = imageio.imread('C:\\Users\\USUARIO\\Desktop\\Physique\\L3\\Numèrique\\TP\\TP5\\image_bruit.PNG')


X2 = np.array(img)
figure(figsize=(4,4))
imshow(X2,cmap=cm.gray)

h = filtreGaussien(3)             
Y = convolution2D(X2,h,True)
figure(figsize=(4,4))
imshow(Y,cmap=cm.gray)

plt.show()



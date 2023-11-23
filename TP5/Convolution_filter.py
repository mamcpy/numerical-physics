"""
L3. Phy Numérique
TP5- Ej7: Filtering by convolution
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
#1 Convolution

X = np.zeros((6,6))
X[3,3] = 1
H = np.ones((3,3))

A = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12],[12,13,14,15]]) # Matrix to filter
B = np.array([[1,1,1],[2,2,2],[3,3,3]]) # Filtering matrix

def convolution(A, B):
    """
    Returns convolution between A and filter B, where it starts by creating C array which is array A but with 0's in the borders so that we can get the convolution of the borders without obtaining error'
    """
    C = np.zeros((A.shape[0] + 2,  A.shape[1] + 2))
    C[1:-1, 1:-1] = A
    Y = np.zeros(A.shape)
    
    for i in range(0, A.shape[0]):
        for j in range(0, A.shape[1]):
            Y[i,j]= np.sum(B * C[i:i+B.shape[0], j:j+B.shape[1]])
    return Y
    
print(convolution(X,H))

#2 Filter of average

H1 = np.ones((3,3))*1/9

im = Image.open("image.jpg")
im_array = np.array(im)
red_channel = im_array[:,:,0] # Takes the red channel from the image stored in a matrix red_channel

def convolution_for_red(im,H1):
    final = np.array(im)
    final[:,:,0], final[:,:,1], final[:,:,2] = final[:,:,0], np.zeros(im.size).T, np.zeros(im.size).T 
    finalimag = Image.fromarray(final)
    plt.imshow(finalimag)
    plt.figure()
    final[:,:,0], final[:,:,1], final[:,:,2] = convolution(final[:,:,0], H1), np.zeros(im.size).T, np.zeros(im.size).T 
    finalimag = Image.fromarray(final)
    plt.imshow(finalimag)
    
convolution_for_red(im,H1)

# Gaussian Filter



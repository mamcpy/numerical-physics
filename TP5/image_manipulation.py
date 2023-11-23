"""
L3. Phy Numérique
TP5- Ej6: Image manipulation
Erasmus: Miguel Angel Martinez Camara
"""

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

im = Image.open("image.jpg")
print("Height and Width", im.height, im.width, "Size", im.size, "Type of pixel", im.mode)
im.show()

im_array = np.array(im)
print("RowsxColumns is", im_array.shape)
im_array[25:125,400:700] = (150, 240, 104) # RGB for light green

# plt.savefig("im_modified.png")
plt.imshow(im_array)
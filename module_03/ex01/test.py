from ImageProcessor import ImageProcessor
from PIL import Image 
import numpy as np


imp = ImageProcessor()
arr = imp.load("gusimone.jpg")
print(arr)
imp.display(arr)


# --> DISPLAY RANDOM MATRIX
# image_matrice = np.random.randint(0, 256, size=(100, 100, 3), dtype=np.uint8)
# imp.display(image_matrice)
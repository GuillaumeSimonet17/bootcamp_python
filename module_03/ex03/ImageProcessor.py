import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

class ImageProcessor:

    def is_empty(self, width, height):
        return width == 0 and height == 0

    def load(self, path):
        try:
            self.img = Image.open(path)
            self.matrix = np.array(self.img)
            width, height = self.img.size
            if self.is_empty(width, height):
                return OSError(" OSError -- strerror: None")
            print(f"Loading image of dimensions {width} x {height}")
            return self.matrix
        except (FileNotFoundError) as e:
            print("FileNotFoundError -- strerror: No such file or directory")

    def display(self, array):
        plt.imshow(array) # interprete les valeur de la matrice comme des valeurs de couleurs
        plt.show() # ouvre la fenetre
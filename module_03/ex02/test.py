import numpy as np
from ScrapBooker import ScrapBooker

spb = ScrapBooker()
# arr1 = np.arange(25).reshape(5,5)
# arr1 = spb.crop(arr1, (3,1),(1,0))

# arr2 = np.array("A B C D E F G H I".split() * 6).reshape(-1,9)
# arr2 = spb.thin(arr2,3,0)

arr3 = np.array([[1, 2, 3],[4, 5, 6],[7, 8, 9]])
arr3 = spb.mosaic(arr3, (3, 3))
print(arr3)
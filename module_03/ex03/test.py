from ColorFilter import ColorFilter
import sys
from ImageProcessor import ImageProcessor


img = ImageProcessor()
elon1 = img.load("elonmusk.jpg")
elon2 = img.load("elonmusk2.png")

obj = ColorFilter()
# try:
#     # arr1 = obj.to_blue(elon1)
#     # img.display(arr1)
#     arr2 = obj.to_celluloid(elon2)
#     img.display(arr2)
# except:
#     print('elon1 ou elon2 not found')
arr2 = obj.to_celluloid(elon2)
img.display(arr2)
# img.display(elon2)
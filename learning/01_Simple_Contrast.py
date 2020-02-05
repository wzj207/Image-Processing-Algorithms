import numpy as np
import cv2
import math

img = cv2.imread('../images/low_contrast_1.jpg',cv2.IMREAD_GRAYSCALE)

height = img.shape[0]
width = img.shape[1]

contrast = 1.3

for i in np.arange(height):
    for j in np.arange(width):
        



cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

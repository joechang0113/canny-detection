import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('test2.jpg', 0)

#canny
img = cv2.GaussianBlur(img, (3, 3), 0)
canny = cv2.Canny(img, 50, 150)

cv2.imshow("canny detection", canny)
# plt.show(img)
cv2.waitKey(0)

import cv2
import numpy as np

img = cv2.imread('images/picture2.jpg')
negative_img = 255 - img
cv2.imshow('Original Image', img)
cv2.imshow('Negative Image', negative_img)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('outputs/negative_image.jpg', negative_img)
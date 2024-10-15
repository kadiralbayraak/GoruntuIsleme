import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('images/picture2.jpg', cv2.IMREAD_GRAYSCALE)

# Kontrast germe (histogram stretching)
min_val = np.min(img)  # Görüntüdeki minimum piksel değeri
max_val = np.max(img)  # Görüntüdeki maksimum piksel değeri

stretched_image = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX)

cv2.imshow('Original Image', img)
cv2.imshow('Stretched Image', stretched_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('outputs/stretched_image.jpg', stretched_image)
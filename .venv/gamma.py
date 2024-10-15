import cv2
import numpy as np

img = cv2.imread("images/picture2.jpg")

gamma = 2.0
inv_gamma = 5.0

table = np.array([((i / 255.0) ** inv_gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")

gamma_corrected = cv2.LUT(img, table)

cv2.imshow('Original Image', img)
cv2.imshow("Gamma Corrected", gamma_corrected)
cv2.waitKey(0)
cv2.destroyAllWindows()

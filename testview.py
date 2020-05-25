import cv2
import numpy as np

img33=cv2.imread("./cameraman.jpg",cv2.IMREAD_UNCHANGED)
print(img33)

cv2.imshow('image',img33)
cv2.waitKey(0)
cv2.destroyAllWindows()


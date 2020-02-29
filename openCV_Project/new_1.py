import cv2
import numpy as np

a = input("Enter name of image = ")


img = cv2.imread("muskan.jpg")

r, c = img.shape[:2]

m = np.float32([[1, 0, 100], [0, 1, 100]])

new_img = cv2.warpAffine(img, m, (c, r))

cv2.imwrite("a.jpg", new_img)

cv2.imshow("translation", new_img)
cv2.waitKey(0)

cv2.destroyAllWindows()

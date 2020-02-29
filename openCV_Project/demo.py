import  cv2
a = input()

img = cv2.imread(a)
img_crop = img[0:2000, 150:350]
cv2.imwrite("crop_img.jpg", img_crop)
cv2.imshow("crop", img_crop)
cv2.waitKey(0)

cv2.destroyAllWindows()

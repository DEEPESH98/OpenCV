# import cv2
# img = cv2.imread("isha.jpg")
#
# new_img = cv2.GaussianBlur(img,(5,5),9) # variba;e dena he
# cv2.imwrite("blur.jpg",new_img)
# cv2.imshow("blur.jpg",new_img)
#
# cv2.waitKey(0)
#
# cv2.destroyAllWindows()


import  cv2
# a = input("Enter Image name = ")
#
img = cv2.imread("isha.jpg")
# img_crop = img[0:2000, 150:350]
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imwrite("new_crop_img.jpg",grayimg)
cv2.imshow("new_crop_img", grayimg)
cv2.waitKey(0)
#
cv2.destroyAllWindows()

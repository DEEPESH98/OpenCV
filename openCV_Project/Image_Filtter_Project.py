import cv2
import numpy as np

while 1!=0:
    print("1: Crop Image")
    print("2: Gray color Image")
    print("3: Translation Image")
    print("4: Image Rotate")
    print("5: Image Blur")
    print("6: HSV Color")
    print("7: HSV to BGR Color")
    print("8: YUV Color")
    print("9: Close the program")
    choice = int(input("Enter a choice = "))

    if choice == 1:
        a = input("Enter Image name = ")
        img = cv2.imread(a)
        img_crop = img[0:2000, 150:350]
        cv2.imwrite("crop_img.jpg", img_crop)
        cv2.imshow("crop", img_crop)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 2:
        a = input("Enter Image name = ")
        img = cv2.imread(a)
        grayimg3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imwrite("new_crop_img.jpg", grayimg3)
        cv2.imshow("new_crop_img", grayimg3)
        cv2.waitKey(0)
        #
        cv2.destroyAllWindows()

    elif choice == 3:
        a = input("Enter Image name = ")
        img = cv2.imread(a)

        r, c = img.shape[:2]

        m = np.float32([[1, 0, 100], [0, 1, 100]])

        new_img = cv2.warpAffine(img, m, (c, r))

        cv2.imwrite("a.jpg", new_img)

        cv2.imshow("translation", new_img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    elif choice == 4:
        a = input("Enter Image name = ")
        img = cv2.imread(a)

        r, c = img.shape[:2]

        m = cv2.getRotationMatrix2D((c / 2, r / 2), 90, 1)

        new_img = cv2.warpAffine(img, m, (c, r))

        cv2.imwrite("rotate.jpg", new_img)
        cv2.imshow("rotate", new_img)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    elif choice == 5:
        a = input("Enter Image name = ")
        img = cv2.imread(a)

        new_img = cv2.GaussianBlur(img, (5, 5), 9)  # variba;e dena he
        cv2.imwrite("blur.jpg", new_img)
        cv2.imshow("blur.jpg", new_img)

        cv2.waitKey(0)

        cv2.destroyAllWindows()

    elif choice == 6:
        a = input("Enter Image name = ")
        img = cv2.imread(a)

        grayimg1 = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        cv2.imwrite("new_crop_img.jpg", grayimg1)
        cv2.imshow("new_crop_img", grayimg1)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    elif choice == 7:
        a = input("Enter Image name = ")
        img = cv2.imread(a)
        grayimg2 = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)

        cv2.imwrite("new_crop_img.jpg", grayimg2)
        cv2.imshow("new_crop_img", grayimg2)
        cv2.waitKey(0)

        cv2.destroyAllWindows()

    elif choice == 8:
        a = input("Enter Image name = ")
        img = cv2.imread(a)
        grayimg3 = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

        cv2.imwrite("new_crop_img.jpg", grayimg3)
        cv2.imshow("new_crop_img", grayimg3)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    elif choice == 9:
        break



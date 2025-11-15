import cv2


img = cv2.imread("cuteasf.jpg")


if img is None:
    print("image not found")
    exit()


h, w = img.shape[:2]


img_small = cv2.resize(img, (w // 4, h // 4))

cv2.imshow("Original Image", img)
cv2.imshow("1/4th Size Image", img_small)

cv2.waitKey(0)
cv2.destroyAllWindows()

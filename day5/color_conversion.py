import cv2


img = cv2.imread("cuteasf.jpg")

if img is None:
    print("Image not found.")
    exit()


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)


cv2.imshow("Original Image", img)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("HSV Image", hsv)
cv2.imshow("LAB Image", lab)

cv2.waitKey(0)
cv2.destroyAllWindows()

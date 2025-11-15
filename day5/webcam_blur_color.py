import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame")
        break

    blur = cv2.GaussianBlur(frame, (15, 15), 0)

    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lab = cv2.cvtColor(frame, cv2.COLOR_BGR2LAB)

   
    cv2.imshow("Original Webcam", frame)
    cv2.imshow("Gaussian Blur", blur)
    cv2.imshow("Gray", gray)
    cv2.imshow("HSV", hsv)
    cv2.imshow("LAB", lab)

   
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

from ultralytics import YOLO
import cv2


model = YOLO("yolo11n-pose.pt") 


print(model.names)


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to read frame")
        break

    results = model(frame, classes=[0], verbose=False)

    annotated_frame = results[0].plot()

    cv2.imshow("YOLO Pose Detection", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

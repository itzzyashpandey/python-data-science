import cv2

video = cv2.VideoCapture(0)

while True:
    check, frame = video .read()
    if not check:
        break
    cv2.imshow("webcam 0", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
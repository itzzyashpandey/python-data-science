import cv2

import cv2

video = cv2.VideoCapture(0)

while True:
    status, frame = video .read()
    #resize
    #print(frame.shape)
    #frame=cv2.resize(frame,(frame.shape[1]//2, frame.shape[0]//2))
    
    cv2.rectangle(frame, (100,100), (200,200), (0,255,0),2)
    cv2.putText(frame,'Live', (150,80),
                cv2.FONT_HERSHEY_PLAIN, 2, (0,0,0),2, cv2.LINE_AA,False)
    cv2.imshow("webcam 0", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    
video.release()
cv2.destroyAllWindows()
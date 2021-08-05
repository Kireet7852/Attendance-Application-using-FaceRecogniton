import cv2
import sys

cascPath="haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades+cascPath)####major error

video_capture=cv2.VideoCapture(0)

while True:
    ret, frame=video_capture.read()
    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces= faceCascade.detectMultiScale(gray, scaleFactor=1.1,minSize=(30,30))

    for(x,y,w,h) in faces:
        cv2.rectangle(frame,(x+w,y+h),(0,255,0),2)
    cv2.imshow('video',frame)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
import cv2
import numpy as np
import time


#eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
leye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
reye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

cap = cv2.VideoCapture(0)
ptime = 0

while cap.isOpened():
    ret,frame = cap.read()
    original = frame.copy()
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    cv2.putText(frame,str(int(fps)),(550,50),cv2.FONT_HERSHEY_PLAIN,3,(0,100,255),3)

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,5,1,1)
    #eye = eye_cascade.detectMultiScale(gray,1.3,5,minSize =(50,50))
    leye = leye_cascade.detectMultiScale(gray,1.1,10)
    reye = reye_cascade.detectMultiScale(gray,1.1,10)
    filename = f'blinked.png'
    if len(leye) >=2 & len(reye) >=2 :
        for (x,y,w,h) in leye:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        for (x,y,w,h) in reye:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,'Open',(20, 60),cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),3)
    else:
        cv2.putText(frame,'Closed',(20, 60),cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),3)
        cv2.imwrite(filename, original)
        
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()

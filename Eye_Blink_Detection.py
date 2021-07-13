import cv2
import numpy as np

#eye_cascade = cv2.CascadeClassifier('haarcascade_eye_tree_eyeglasses.xml')
leye_cascade = cv2.CascadeClassifier('haarcascade_lefteye_2splits.xml')
reye_cascade = cv2.CascadeClassifier('haarcascade_righteye_2splits.xml')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray,5,1,1)
    #eye = eye_cascade.detectMultiScale(gray,1.3,5,minSize =(50,50))
    leye = leye_cascade.detectMultiScale(gray,1.1,10)
    reye = reye_cascade.detectMultiScale(gray,1.1,10)
    blinked = 0
    if len(leye) >=2 & len(reye) >=2 :
        for (x,y,w,h) in leye:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        for (x,y,w,h) in reye:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.putText(frame,'Open',(20, 60),cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),3)
    else:
        #blinked +=1
        cv2.putText(frame,'Closed',(50, 60),cv2.FONT_HERSHEY_SIMPLEX, 2,(255,0,0),3)

    #if blinked >=1 & blinked <=6:
        #cv2.putText(frame,'Blinked',(50, 50),cv2.FONT_HERSHEY_SIMPLEX, 3,(255,0,0),5)



    cv2.imshow('frame',frame)
    cv2.waitKey(1)

cap.release()

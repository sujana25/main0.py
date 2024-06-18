import cv2
from cvzone.HandTrackingModule import HandDetector
detector=HandDetector(detectionCon=0.8,maxHands=1)
video=cv2.VideoCapture(0)
while True:
    ret,frame=video.read()
    hands,img=detector.findHands(frame)
    cv2.rectangle(img,(0,480),(300,425),(50,50,255),-2)
    cv2.rectangle(img,(640,480),(400,425),(50,50,255),-2)
    if hands:
        lmlist=hands[0]
        fingureup=detector.fingersUp(lmlist)
        print(fingureup)
        if fingureup==[0,0,0,0,0]:
            cv2.putText(frame,'Finger Count:0',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'Jumping',(420,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if fingureup==[0,1,0,0,0]:
            cv2.putText(frame,'Finger Count:1',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'NotJumping',(420,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if fingureup==[0,1,1,0,0]:
            cv2.putText(frame,'Finger Count:2',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'NotJumping',(420,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if fingureup==[0,1,1,1,0]:
            cv2.putText(frame,'Finger Count:3',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'NotJumping',(420,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if fingureup==[0,1,1,1,1]:
            cv2.putText(frame,'Finger Count:4',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'NotJumping',(420,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        if fingureup==[1,1,1,1,1]:
            cv2.putText(frame,'Finger Count:5',(20,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
            cv2.putText(frame,'NotJumping',(420,460),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),1,cv2.LINE_AA)
        
    cv2.imshow("Frame",frame)
    k=cv2.waitKey(1)
    if k==ord('q'):
        break
video.release()

cv2.destoryAllWindows()

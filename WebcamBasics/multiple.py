import cv2

cam=cv2.VideoCapture(0)

while True:
    ignore ,frame= cam.read();
    grayframe=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Normal1',frame)
    cv2.moveWindow('Normal1',0,0)
    cv2.imshow('Grey1',grayframe)
    cv2.moveWindow('Grey1',640,0)
    cv2.imshow('Normal2',frame)
    cv2.moveWindow('Normal2',640,480)
    cv2.imshow('Grey2',grayframe)
    cv2.moveWindow('Grey2',0,480)

    if cv2.waitKey(1)&0xff==ord('q'):
        break;
cam.release()
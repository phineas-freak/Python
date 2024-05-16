import cv2
print(cv2.__version__)

width=640
height=360
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH,width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,height)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))

while True:
    ignore, frame =cam.read()
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('Normal1',frame)
    cv2.moveWindow('Normal1',0,0)
    cv2.imshow('gray1',gray)
    cv2.moveWindow('gray1',640,0)
    cv2.imshow('gray2',gray)
    cv2.moveWindow('gray2',0,360)
    cv2.imshow('my WEBcam',frame)
    cv2.moveWindow('my WEBcam',640,360)
    if cv2.waitKey(1) &0xff == ord('q'):
        break
cam.release()
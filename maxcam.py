import cv2
cam=cv2.VideoCapture(0,cv2.CAP_DSHOW)

h=1080
w=1920
row=int(input("Rows: "))
columns=int(input("Columns: "))


cam.set(cv2.CAP_PROP_FRAME_WIDTH,w)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT,h)
cam.set(cv2.CAP_PROP_FPS,30)
cam.set(cv2.CAP_PROP_FOURCC,cv2.VideoWriter_fourcc(*'MJPG'))
i=0
j=0

while True:
    ignore, frame=cam.read()
    frame=cv2.resize(frame,(int(w/columns),int(h/columns)))
    for i in range(0,row):
        for j in range(0,columns):
            winname='win'+str(i)+' '+str(j) 
            cv2.imshow(winname,frame)
            cv2.moveWindow(winname,int(w/columns)*j,int(h/columns+30)*i)
           

    if cv2.waitKey(1)&0xff==ord('q'):
        break

cam.release()


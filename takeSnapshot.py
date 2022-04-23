import cv2
def takeSnapshot():
    captureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=captureObject.read()
        cv2.imwrite("Pic1.jpg",frame)
        result=False
    captureObject.release()
    cv2.destroyAllWindows()
takeSnapshot()   
    

 
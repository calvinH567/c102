from tkinter import image_names
import cv2
import dropbox
import time
import random
startTime=time.time()
def takeSnapshot():
    number=random.randint(0,10)
    captureObject=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=captureObject.read()
        imageName="img"+str(number)+".png"
        cv2.imwrite(imageName,frame)
        startTime=time.time
        result=False
    return imageName
    print("snapshotTaken")
    captureObject.release()
    cv2.destroyAllWindows()
takeSnapshot()   
def uploadFile(imageName):
    access_token="sl.BFUOaFsF0rfwwnvffu_vzWhvKAIF43EPqgDbGdFnXy8v8kgiQFUtzc76NxwGbFTpFfPYPvqIhbMk2uMZSIHeviW06bt9dgugINPLnuNh3oLajcA5CI5YQBEWIZ23GUIjPP3ME2-h_R8k"
    file=imageName
    fileFrom=file
    fileto="/testfolder/"+(imageName)
    dbx=dropbox.Dropbox(access_token)
    with open(fileFrom,'rb') as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("file Has Been Uploadded")
def main():
    while(True):
        if((time.time()-startTime)>=5):
            name=takeSnapshot()
            uploadFile(name)
main()
import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime
path ='imageattendance'
images=[]
classnames=[]
mylist = os.listdir(path)
print(mylist)
for cl in mylist:
    curimg =cv2.imread(f'{path}/{cl}')
    images.append(curimg)
    classnames.append(os.path.splitext(cl)[0])
print(classnames)
def findencodings(images):
    encodelist=[]
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist
def markattendance(name):
    with open('attendance.csv','r+') as f:
        mydata = f.readlines()
        namelist=[]
        for line in mydata:
            entry = line.split(',')
            namelist.append(entry[0])
        if name not in namelist:
            now = datetime.now()
            dtstring = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtstring}')

encodelistknown = findencodings(images)
print(len(encodelistknown))
cap =cv2.VideoCapture(0)
while True:
    ret,frame= cap.read()
    imgs = cv2.resize(frame,(0,0),None,0.25,0.25)
    imgs = cv2.cvtColor(imgs,cv2.COLOR_BGR2RGB)
    currfaceloc = face_recognition.face_locations(imgs)
    currfaceencode = face_recognition.face_encodings(imgs,currfaceloc)
    for fe,fl in zip(currfaceencode,currfaceloc):
        match = face_recognition.compare_faces(encodelistknown,fe)
        facedis = face_recognition.face_distance(encodelistknown,fe)
        #print(facedis)
        matchindex = np.argmin(facedis)
        if(match[matchindex]):
            name = classnames[matchindex].upper()
            #print(name)
            y1, x2, y2, x1 = fl
            y1, x2, y2, x1 = y1*4,x2*4,y2*4,x1*4
            cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
            cv2.rectangle(frame,(x1,y2-35),(x2,y2),(0,255,0),cv2.FILLED)
            cv2.putText(frame,name,(x1+6,y2-6),cv2.FONT_HERSHEY_COMPLEX,1,(255,255,255),2)
            markattendance(name)
    cv2.imshow('Webcam',frame)
    cv2.waitKey(0)



import cv2
import numpy as np
import face_recognition
imgbillgates = face_recognition.load_image_file('imgbillgates.jpg')
imgbillgates=cv2.cvtColor(imgbillgates,cv2.COLOR_BGR2RGB)
testbillgates = face_recognition.load_image_file('testbillgates.jpg')
testbillgates=cv2.cvtColor(testbillgates,cv2.COLOR_BGR2RGB)
faceloc = face_recognition.face_locations(imgbillgates)[0]
encodeface = face_recognition.face_encodings(imgbillgates)[0]
cv2.rectangle(imgbillgates,(faceloc[3],faceloc[0]),(faceloc[1],faceloc[2]),(255,0,255),2)
faceloctest = face_recognition.face_locations(testbillgates)[0]
encodefacetest = face_recognition.face_encodings(testbillgates)[0]
cv2.rectangle(testbillgates,(faceloctest[3],faceloctest[0]),(faceloctest[1],faceloctest[2]),(255,0,255),2)
compare = face_recognition.compare_faces([encodeface],encodefacetest)
facedis = face_recognition.face_distance([encodeface],encodefacetest)
print(compare,facedis)
cv2.putText(imgbillgates,f'{compare} {round(facedis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
cv2.imshow("Bill Gates",imgbillgates)
cv2.imshow("Bill Gates Test Image",testbillgates)
cv2.waitKey(0)

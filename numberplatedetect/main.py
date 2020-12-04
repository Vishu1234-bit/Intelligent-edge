import cv2
import pytesseract
import numpy as np
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
cascade = cv2.CascadeClassifier('haarcascade_russian_plate_number.xml')
img = cv2.imread('car1.JPG')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
nplate = cascade.detectMultiScale(gray_img,1.1,4)
for (x,y,w,h) in nplate:
    a,b = (int(0.02*img.shape[0]),int(0.025*img.shape[1]))
    plate = img[y+a+a-1:y+h-a,x+b+b-1:x+w-b]
    kernel = np.ones((1,1),np.uint8)
    plate = cv2.dilate(plate,kernel,iterations=1)
    plate = cv2.erode(plate,kernel,iterations=1)
    plate_gray = cv2.cvtColor(plate,cv2.COLOR_BGR2GRAY)
    (thresh,plate) =cv2.threshold(plate_gray,125,350,cv2.THRESH_BINARY)
    read = pytesseract.image_to_string(plate)
img = cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 3)
img = cv2.putText(img, read, (x-100,y-50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2, cv2.LINE_AA)
print("License Plate :", read)
print(nplate)
cv2.imshow("License Plate Detection",img)
cv2.waitKey(0)
import cv2
import numpy as np
cap = cv2.VideoCapture(0)
#frame = cv2.imread('black.jpg')
while(1):
    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    threshold,thresh = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
    if(cv2.countNonZero(thresh) == 0):
        print("black")
    else:
        print("not black")
    #cv2.imshow("capture",gray)
    # if(cv2.countNonZero(gray)>=0 ):
    #     print("black image")
    # else:
    #     print("coloured image")
    # count = cv2.countNonZero(gray)
    # print(count)
    if(cv2.waitKey(5)==27):
          break
cv2.destroyAllWindows()
# import cv2
# image = cv2.imread("black.jpg", 0)
# count = cv2.countNonZero(image)
# print(count)

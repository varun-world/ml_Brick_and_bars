import cv2
import numpy as np
# created to reflect changes in trackbar continus in image
def empty(a):
    pass

path ="rd/2.jpeg"
cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars",640,240)


#Hue is scale that generate by trackbar to control varius thing have max value 360 but hear we can access only 179
cv2.createTrackbar("Hue Min","TrackBars",3,179,empty)
cv2.createTrackbar("Hue Max","TrackBars",12,179,empty)
cv2.createTrackbar("sat Min","TrackBars",75,255,empty)
cv2.createTrackbar("sat Max","TrackBars",255,255,empty)
cv2.createTrackbar("val Min","TrackBars",68,255,empty)
cv2.createTrackbar("val Max","TrackBars",249,255,empty)

while True:
    img = cv2.imread(path)
    #convert image to HSV
    imgHSV = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    h_min = cv2.getTrackbarPos('Hue Min',"TrackBars")
    h_max = cv2.getTrackbarPos('Hue Max', "TrackBars")
    s_min = cv2.getTrackbarPos('sat Min', "TrackBars")
    s_max = cv2.getTrackbarPos('sat Max', "TrackBars")
    v_min = cv2.getTrackbarPos('val Min', "TrackBars")
    v_max = cv2.getTrackbarPos('val Max', "TrackBars")
    print(h_min,h_max,s_min,s_max,v_max,v_min)
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])
    mask = cv2.inRange(imgHSV,lower,upper)
    #resize = cv2.resize(img,(300,300))
    imgResult = cv2.bitwise_and(img,img,mask=mask)
    # imgStack = stackImages(3.5, ([img, imgHSV, mask,imgResult]))


    cv2.imshow("image",img)
    cv2.imshow("imageHSV",imgHSV)
    cv2.imshow("mask", mask)
    cv2.imshow("image", imgResult)
    #cv2.imshow("ImageStack", imgStack)
    cv2.waitKey(1)
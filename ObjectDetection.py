import cv2
import numpy as np
import argparse
import Utilities
##########################
heightImg=640
widthImg=480
##########################

img = cv2.imread('images4.jpg')




imgBlank=np.zeros((heightImg, widthImg, 3), np.uint8)
img=cv2.resize(img,(widthImg, heightImg))
imgGray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGray,(5,5),1)
r, thresh=cv2.threshold(img, 127, 255, 0)

imgCanny=cv2.Canny(imgBlur,50,200, apertureSize=3)
lines=cv2.HoughLines(imgCanny,1, np.pi/80,200)

kernel=np.ones((3,3))
imgDial=cv2.dilate(imgCanny, kernel, iterations=6)

countour, h= cv2.findContours(imgDial, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

threshold_area = 100
contour=[]#threshold area
maxArea=0
for cnt in countour:
    area = cv2.contourArea(cnt)
    if(area>maxArea):
        maxArea=area
        c=cnt
    if area > threshold_area:
        contour.append(cnt)
x, y, w, h = cv2.boundingRect(c)
cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
#print(c)
extLeft = tuple(c[c[:, :, 0].argmin()][0])
extRight = tuple(c[c[:, :, 0].argmax()][0])
extTop = tuple(c[c[:, :, 1].argmin()][0])
extBot = tuple(c[c[:, :, 1].argmax()][0])
# print(extLeft)
# print(extRight)
#cv2.drawContours(img, [c], -1, (0, 255, 255), 2)
cv2.circle(img, extLeft, 8, (0, 0, 255), -1)
cv2.circle(img, extRight, 8, (0, 255, 0), -1)
cv2.circle(img, extTop, 8, (255, 0, 0), -1)
cv2.circle(img, extBot, 8, (255, 255, 0), -1)

cv2.drawContours(img, c, -1, (0, 255, 0), 3)
cv2.imshow("Image",img)





# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="images4.jpg")
# args = vars(ap.parse_args())
# # load the image and define the window width and height
# image = cv2.imread(args["image"])
# (winW, winH) = (128, 128)
#
# for resized in pyramid(img, scale=1.5):
#
# 	for (x, y, window) in sliding_window(resized, stepSize=32, windowSize=(winW, winH)):
# 		if window.shape[0] != winH or window.shape[1] != winW:
# 			continue
# 		clone = resized.copy()
# 		cv2.rectangle(clone, (x, y), (x + winW, y + winH), (0, 255, 0), 2)
# 		cv2.imshow("Window", clone)
# 		cv2.waitKey(0)
# 		time.sleep(0.025)


cv2.waitKey(0)








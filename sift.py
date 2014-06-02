# purpose : program to obtain sift keypoints from an image
# precaution : since the sift and surf algorithms are not free it is not includede with ordinary opencv installations i did the coding in 
#Ubuntu with ROS Hydra installed


import cv2
import numpy as np

img=cv2.imread("python.jpg",0) #give your image path here
img3=cv2.imread("python.jpg")

sift = cv2.SIFT()
kp = sift.detect(img,None)

img1=cv2.drawKeypoints(img3,kp)


cv2.imwrite('sift.jpg',img1)
cv2.imshow('finalimage',img1)
cv2.waitKey()

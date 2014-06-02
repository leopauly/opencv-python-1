purpose : extraction of corners using FAST (features from accelerated segmented test ) algorithm
author : @leopauly  (meetleopauly@yahoo.com)


import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('corner.jpg',0)
img4=cv2.imread('corner.jpg')


fast = cv2.FastFeatureDetector()
kp = fast.detect(img,None)

img2=cv2.drawKeypoints(img4, kp, color=(255,0,0))
cv2.imshow('with_NonMax_Sup',img2)

print len(kp)


fast.setBool('nonmaxSuppression',0)
kp = fast.detect(img,None)
print len(kp)

img3=cv2.drawKeypoints(img4, kp, color=(255,0,0))
cv2.imshow('without_nonmax_sup',img3)
cv2.waitKey()

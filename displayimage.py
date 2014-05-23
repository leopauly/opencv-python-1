#-------------------------------------------------------------------------------
# Name:        displayimage.py
# Purpose:     code to display image and its size
# Author:      leopauly
# Created:     23-05-2014
#-------------------------------------------------------------------------------

import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('logo.jpg',1)
r,c,m=img.shape
print(r,c,m)
cv2.imshow('image',img)
cv2.waitKey()

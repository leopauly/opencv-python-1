#-------------------------------------------------------------------------------
# Name : skeleton.py
# Purpose: skeletonization
# Author: leopauly (meetleopauly@yahoo.com)
# Created: 26-05-2014
# Steps :
# 1)Blur with gaussian function
# 2)Threshold with otsus binariasation
# 3)Inverted the image so that white is forground and black is back ground
# 4) Then used  morphological functions erode and dilate continuosly until
#    the very narrow skeleton was obtained
#-------------------------------------------------------------------------------

def main():
    import cv2
    import numpy as np

    img=cv2.imread('mal2.jpg',0)
    size=np.size(img)
    skel=np.zeros(img.shape,np.uint8)

    blur= cv2.GaussianBlur(img,(5,5),0)
    ret,thrs=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    inv=cv2.bitwise_not(thrs)

    element = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(3,3))
    done = False

    while( not done):
     eroded = cv2.erode(inv,element)
     temp = cv2.dilate(eroded,element)
     temp = cv2.subtract(inv,temp)
     skel = cv2.bitwise_or(skel,temp)
     inv = eroded.copy()

     zeros = size - cv2.countNonZero(inv)
     if zeros==size:
        done = True


    cv2.imshow('skel',skel)
    cv2.waitKey()

if __name__ == '__main__':
    main()

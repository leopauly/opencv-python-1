#-------------------------------------------------------------------------------
# Name:        contours.py
# Purpose:     --find the largest of all contours in the given image
#              --find and plot its centroid
# Author:      leopauly (meetleopauly@yahoo.com)
# Created:     28-05-2014
#-------------------------------------------------------------------------------

def main():
     import cv2
     import numpy as np

     img=cv2.imread('tomato.jpg')  # give ur image path
     cv2.imshow('image1',img)
     print(img.shape)

     gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
     cv2.imshow('image2',gray)
     ret,thrs=cv2.threshold(gray,127,255,0)
     cv2.imshow('image',thrs)

     print(thrs.shape)
     conts,h=cv2.findContours(thrs,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

     a=0
     n=len(conts)
     for i in range(1,n):
        if(len(conts[i])>a):
            big=i
            a=len(conts[i])

     cv2.drawContours(img,conts,big,(0,0,0),2)
     cv2.imshow('image5',img)

     M=cv2.moments(conts[big])

     x_c=int(M['m10']/M['m00'])
     y_c=int(M['m01']/M['m00'])

     print (x_c,y_c)

     cv2.circle(img,(x_c,y_c),6,-1)
     cv2.imshow('image6',img)
     cv2.waitKey(0)

if __name__ == '__main__':
    main()

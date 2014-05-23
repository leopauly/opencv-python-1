#-------------------------------------------------------------------------------
# Name:        resize.py
# Purpose:     python code to resize the give image
# Author:      leopauly
# Created:     23-05-2014
#-------------------------------------------------------------------------------

def main():
    import cv2
    import numpy as np


    img=cv2.imread('logo.png',0) #change the name of image.
    #Give complete path if the image is not in the working directory.
    m,n=img.shape
    size=np.float32([[1,0,100],[0,1,50]])
    new = cv2.warpAffine(img,size,(m,n))

    cv2.imshow('pic',img)
    cv2.imshow('pic1',new)
    cv2.waitKey()



if __name__ == '__main__':
    main()

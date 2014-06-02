#purpose : to filter out only red colored portions from the image
#author :  @leopauly (meetleopauly@yahoo.com)



import cv2
import numpy as np

img = cv2.imread("python.jpg",-1)
cv2.imshow("opencv",img)

blur=cv2.GaussianBlur(img,(5,5),0)
cv2.imshow("opencv4",blur)
hsv=cv2.cvtColor(blur,cv2.COLOR_BGR2HSV)

lower=np.array([0,100,100])
upper=np.array([20,255,255])
mask=cv2.inRange(hsv,lower,upper)
cv2.imshow("opencv3",mask)
out=cv2.bitwise_and(img,img,mask=mask)
cv2.imshow("opencv2",out)

cv2.waitKey(0)

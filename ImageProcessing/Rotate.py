'''
We can rotatte image by using python
Syntax: cv2.cv.rotate( src, rotateCode[, dst] )
'''
# Load the image
import cv2

image = cv2.imread('ImageProcessing/arrow.png')
image_rotate_90 = cv2.rotate(image,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('image_rotate_90', image_rotate_90)

image_rotate_counter_90 = cv2.rotate(image,cv2.ROTATE_90_COUNTERCLOCKWISE)
cv2.imshow('image_rotate_counter_90', image_rotate_counter_90)

image_rotate_180 = cv2.rotate(image,cv2.ROTATE_180)
cv2.imshow('image_rotate_180', image_rotate_180)


cv2.waitKey(10000) #Wait till 10000 milliseconds
cv2.destroyAllWindows()


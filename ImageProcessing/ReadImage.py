'''
Image processing in Python is widely usedin multiple applications. 
It helps us in a number of industries medical imaging,security, vision, infrastructure, etc. 
In this process, we can modify, and analyzeimages by using computer algorithms.In Python, 
we can use OpenCV, an open-source packagethat helps us with image processing computer vision, etc.
It supports multiple programminglanguages including Python, C++, and Java. OpenCV is highly tuned for real-timeapplications and has many capabilities.
'''
# In this blog we will first understand how to read and write image by python.
import cv2

  
# Load the image
image = cv2.imread('ImageProcessing/python.png')

#write image
cv2.imwrite('ImageProcessing/python-new.png',image)
#print(image)
print(image.shape)
print(image.size)



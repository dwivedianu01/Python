'''
Choice of Interpolation Method for Resizing:

cv2.INTER_AREA: This is used when we need to shrink an image.
cv2.INTER_CUBIC: This is slow but more efficient.
cv2.INTER_LINEAR: This is primarily used when zooming is required. This is the default interpolation technique in OpenCV.
Syntax: cv2.resize(source, dsize, dest, fx, fy, interpolation)


'''
import cv2


  
# Load the image
image = cv2.imread('ImageProcessing/python.png')
#Resize image
small = cv2.resize(image, (0, 0), fx = 0.5, fy = 0.5)
big = cv2.resize(image, (0, 0), fx = 2.0, fy = 2.0)
stretch = cv2.resize(image, (0, 0), fx = 4.0, fy = 4.0,
                interpolation =cv2.INTER_LINEAR)


cv2.imwrite('ImageProcessing/python-small.png',small)
cv2.imwrite('ImageProcessing/python-big.png',big)
cv2.imwrite('ImageProcessing/python-stretch.png',stretch)
#print(image)
print(f"Actual image shape {image.shape}")
print(f"Small image shape {small.shape}")
print(f"Big image shape {big.shape}")
print(f"Stretch image shape {stretch.shape}")

print(f"Actual image size {image.size}")
print(f"Actual image size {small.size}")
print(f"Actual image size {big.size}")
print(f"Stretch image size {stretch.size}")





import cv2
import numpy as np

# Read the image
image = cv2.imread('img2.jpeg')

# Check if the image is loaded successfully
if image is None:
    print("Could not read the image. Please check the file path.")
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply edge detection using different operators

# Sobel operator
sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobel_x, sobel_y)



# Laplacian operator
laplacian = cv2.Laplacian(gray, cv2.CV_64F)

# Canny edge detector
canny = cv2.Canny(gray, 100, 200)

# Display the original and edge-detected images using different operators
cv2.imshow('Original Image', image)
cv2.imshow('Sobel Operator', sobel.astype(np.uint8))
cv2.imshow('Laplacian Operator', laplacian.astype(np.uint8))
cv2.imshow('Canny Edge Detector', canny)
cv2.waitKey(0)
cv2.destroyAllWindows()

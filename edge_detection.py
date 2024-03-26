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

# Apply Median filter for noise reduction and edge detection
median = cv2.medianBlur(gray, 5)  # Change the kernel size as required

# Apply Laplacian for edge enhancement
laplacian = cv2.Laplacian(median, cv2.CV_64F)

# Convert the result back to 8-bit image
edges = cv2.convertScaleAbs(laplacian)

# Display the original and edge-detected images
cv2.imshow('Original Image', image)
cv2.imshow('Edge Detected Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()



import cv2
import numpy as np

# Load an image
image = cv2.imread('img2.jpeg')

# Display the original image
cv2.imshow('Original Image', image)
cv2.waitKey(0)

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Display the grayscale image
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)

# Apply Gaussian Blur
gaussian_blur = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Display the image after Gaussian Blur
cv2.imshow('Gaussian Blur', gaussian_blur)
cv2.waitKey(0)

# Apply Median Blur
median_blur = cv2.medianBlur(gray_image, 5)

# Display the image after Median Blur
cv2.imshow('Median Blur', median_blur)
cv2.waitKey(0)

# Apply Bilateral Filter
bilateral_filter = cv2.bilateralFilter(gray_image, 9, 75, 75)

# Display the image after Bilateral Filter
cv2.imshow('Bilateral Filter', bilateral_filter)
cv2.waitKey(0)

# Apply Histogram Equalization
equalized_image = cv2.equalizeHist(gray_image)

# Display the image after Histogram Equalization
cv2.imshow('Histogram Equalization', equalized_image)
cv2.waitKey(0)

# Apply Thresholding
_, thresholded_image = cv2.threshold(gray_image, 127, 255, cv2.THRESH_BINARY)

# Display the image after Thresholding
cv2.imshow('Thresholding', thresholded_image)
cv2.waitKey(0)

# Apply Adaptive Thresholding
adaptive_threshold = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)

# Display the image after Adaptive Thresholding
cv2.imshow('Adaptive Thresholding', adaptive_threshold)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

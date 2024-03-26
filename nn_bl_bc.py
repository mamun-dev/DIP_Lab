import cv2

# Load an image
image = cv2.imread('img2.jpeg')

# Define the new dimensions
new_width = 300
new_height = 200

# Nearest Neighbor Interpolation
nearest_neighbor = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_NEAREST)

# Bilinear Interpolation
bilinear = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_LINEAR)

# Bicubic Interpolation
bicubic = cv2.resize(image, (new_width, new_height), interpolation=cv2.INTER_CUBIC)

# Display the original and resampled images
cv2.imshow('Original Image', image)
cv2.imshow('Nearest Neighbor Interpolation', nearest_neighbor)
cv2.imshow('Bilinear Interpolation', bilinear)
cv2.imshow('Bicubic Interpolation', bicubic)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

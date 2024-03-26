import cv2

# Load an image
image = cv2.imread('img2.jpeg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Non-Local Means Denoising
denoised_image = cv2.fastNlMeansDenoising(gray_image, None, h=10, templateWindowSize=7, searchWindowSize=21)

# Display the original and denoised images
cv2.imshow('Original Image', gray_image)
cv2.imshow('Denoised Image', denoised_image)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

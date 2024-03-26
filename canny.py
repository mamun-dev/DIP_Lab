import cv2
import matplotlib.pyplot as plt

# Read the image
image = cv2.imread('img2.jpeg', 0)  # Read image as grayscale

if image is not None:
    # Apply Canny edge detection
    edges = cv2.Canny(image, 100, 200)  # You can adjust the thresholds for edge detection

    # Display the original image and the detected edges
    plt.figure(figsize=(10, 5))

    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap='gray')
    plt.title('Original Image')
    plt.axis('off')

    plt.subplot(1, 2, 2)
    plt.imshow(edges, cmap='gray')
    plt.title('Canny Edge Detection')
    plt.axis('off')

    plt.show()
else:
    print("Error: Unable to read the image. Please check the file path.")
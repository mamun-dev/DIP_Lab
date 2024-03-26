import cv2
import matplotlib.pyplot as plt

# Read the grayscale image
image_gray = cv2.imread('grayscale.jpg', cv2.IMREAD_GRAYSCALE)

if image_gray is not None:
    # Calculate the histogram
    hist_gray = cv2.calcHist([image_gray], [0], None, [256], [0, 256])

    # Display the histogram
    plt.figure(figsize=(8, 5))
    plt.plot(hist_gray, color='black')
    plt.title('Grayscale Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()
else:
    print("Error: Unable to read the grayscale image. Please check the file path.")
import cv2
import matplotlib.pyplot as plt

# Read the color image
image_color = cv2.imread('img.jpg')

if image_color is not None:
    # Calculate the histogram for each channel (BGR)
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        hist = cv2.calcHist([image_color], [i], None, [256], [0, 256])
        plt.plot(hist, color=col)

    # Display the histogram
    plt.title('Color Image Histogram')
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.legend(['Blue', 'Green', 'Red'])
    plt.show()
else:
    print("Error: Unable to read the color image. Please check the file path.")
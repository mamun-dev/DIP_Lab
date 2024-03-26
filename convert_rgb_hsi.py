import cv2
import numpy as np

def rgb_to_hsi(image):
    """
    Convert RGB image to HSI color space.
    """
    r, g, b = cv2.split(image.astype(float))
    intensity = (r + g + b) / 3.0
    minimum = np.minimum.reduce([r, g, b])
    saturation = 1 - minimum / intensity
    saturation[np.where(intensity == 0)] = 0
    theta = np.arccos((0.5 * ((r - g) + (r - b))) / (np.sqrt((r - g)**2 + (r - b) * (g - b)) + 1e-8))
    hue = theta.copy()
    hue[np.where(b > g)] = 2 * np.pi - hue[np.where(b > g)]
    hue *= 180 / np.pi
    return cv2.merge([hue, saturation * 255, intensity])

def hsi_to_rgb(image):
    """
    Convert HSI image to RGB color space.
    """
    hue, saturation, intensity = cv2.split(image.astype(float))
    hue *= np.pi / 180
    r = np.zeros_like(hue)
    g = np.zeros_like(hue)
    b = np.zeros_like(hue)
    # RG sector (0 <= H < 120)
    b[np.where((0 <= hue) & (hue < 2 * np.pi / 3))] = intensity[np.where((0 <= hue) & (hue < 2 * np.pi / 3))] * (1 - saturation[np.where((0 <= hue) & (hue < 2 * np.pi / 3))])
    r[np.where((0 <= hue) & (hue < 2 * np.pi / 3))] = intensity[np.where((0 <= hue) & (hue < 2 * np.pi / 3))] * (1 + (saturation[np.where((0 <= hue) & (hue < 2 * np.pi / 3))] * np.cos(hue[np.where((0 <= hue) & (hue < 2 * np.pi / 3))]) / np.cos(np.pi / 3 - hue[np.where((0 <= hue) & (hue < 2 * np.pi / 3))])))
    g = 3 * intensity - (r + b)
    # BG sector (120 <= H < 240)
    r[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))] = intensity[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))] * (1 - saturation[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))])
    g[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))] = intensity[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))] * (1 + (saturation[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))] * np.cos(hue[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))] - 2 * np.pi / 3) / np.cos(np.pi - hue[np.where((2 * np.pi / 3 <= hue) & (hue < 4 * np.pi / 3))])))
    b = 3 * intensity - (r + g)
    # BR sector (240 <= H < 360)
    g[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))] = intensity[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))] * (1 - saturation[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))])
    b[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))] = intensity[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))] * (1 + (saturation[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))] * np.cos(hue[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))] - 4 * np.pi / 3) / np.cos(5 * np.pi / 3 - hue[np.where((4 * np.pi / 3 <= hue) & (hue < 2 * np.pi))])))
    r = 3 * intensity - (g + b)
    return cv2.merge([b, g, r])

# Load an image
image = cv2.imread('img2.jpeg')

# Convert RGB to HSI
hsi_image = rgb_to_hsi(image)

# Convert HSI back to RGB
rgb_image = hsi_to_rgb(hsi_image)

# Display the original, HSI, and converted RGB images
cv2.imshow('Original Image', image)
cv2.imshow('HSI Image', hsi_image.astype(np.uint8))
cv2.imshow('Converted RGB Image', rgb_image.astype(np.uint8))
cv2.waitKey(0)
cv2.destroyAllWindows()

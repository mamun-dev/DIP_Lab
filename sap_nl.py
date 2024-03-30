import cv2
import numpy as np

def median_filter(img, kernel_size):
    filtered_img = img.copy()
    offset = kernel_size // 2

    for i in range(offset, img.shape[0] - offset):
        for j in range(offset, img.shape[1] - offset):
            for k in range(img.shape[2]):  # Loop over each channel
                window = img[i - offset:i + offset + 1, j - offset:j + offset + 1, k]
                median_value = int(np.median(window))
                filtered_img[i, j, k] = median_value

    return filtered_img

def remove_salt_and_pepper_noise(img_path, output_path, kernel_size):
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Unable to read the image.")
        return

    filtered_img = median_filter(img, kernel_size)

    cv2.imwrite(output_path, filtered_img)
    print("Salt-and-pepper noise removed. Filtered image saved as", output_path)

if __name__ == "__main__":
    input_image_path = "img.jpg"
    output_image_path = "sap_removed.jpg"
    kernel_size = 3  # Adjust kernel size as needed

    remove_salt_and_pepper_noise(input_image_path, output_image_path, kernel_size)

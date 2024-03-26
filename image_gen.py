import cv2
import numpy as np

# Create a color image
width = 400
height = 300

# Create a blue image
blue_color = np.zeros((height, width, 3), dtype=np.uint8)
blue_color[:, :] = (255, 0, 0)  # Set BGR color (blue)

# Display the created image
cv2.imshow('Generated Image', blue_color)
cv2.waitKey(0)

# Write the created image to a file
output_filename = 'generated_image.jpg'
cv2.imwrite(output_filename, blue_color)
print(f"Image saved as {output_filename}")

# Read the created image
read_image = cv2.imread(output_filename)

# Display the read image
cv2.imshow('Read Image', read_image)
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

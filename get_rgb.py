import cv2

# Function to get color values on mouse click
def get_color(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        # Extract BGR values from the clicked pixel
        b, g, r = img[y, x]
        print(f"R: {r}, G: {g}, B: {b}")

# Load an image
image_path = 'img2.jpeg'  # Replace 'your_image_path.jpg' with your image path
img = cv2.imread(image_path)

# Check if the image is loaded successfully
if img is None:
    print("Could not read the image. Please check the file path.")
    exit()

# Display the image
cv2.imshow('Image', img)
cv2.setMouseCallback('Image', get_color)

# Wait for user interaction
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2

# Load the image
image = cv2.imread('6.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)  # Adjust thresholds as needed

# Display the original image and the segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', edges)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import numpy as np

# Load the image
image = cv2.imread('5.jpg')

# Convert the image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply the Prewitt operator for edge detection
kernel_x = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
kernel_y = np.array([[-1, -1, -1], [0, 0, 0], [1, 1, 1]])

prewitt_x = cv2.filter2D(gray_image, -1, kernel_x)
prewitt_y = cv2.filter2D(gray_image, -1, kernel_y)

# Combine the results to get the final edge-detected image
prewitt_edges = cv2.addWeighted(cv2.convertScaleAbs(prewitt_x), 0.5,
                                cv2.convertScaleAbs(prewitt_y), 0.5, 0)

# Threshold the edges to get a binary image
_, segmented_image = cv2.threshold(prewitt_edges, 50, 255, cv2.THRESH_BINARY)

# Display the original image and the segmented image
cv2.imshow('Original Image', image)
cv2.imshow('Segmented Image', segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

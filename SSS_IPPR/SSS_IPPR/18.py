import cv2
import numpy as np

# Load two grayscale images
image1 = cv2.imread('18_1.jpg', cv2.IMREAD_GRAYSCALE)
image2 = cv2.imread('18_2.jpg', cv2.IMREAD_GRAYSCALE)

# Check if images are loaded properly
if image1 is None or image2 is None:
    print("Error loading images.")
    exit()

# Ensure both images have the same dimensions
if image1.shape != image2.shape:
    print("Images must have the same dimensions.")
    exit()

# Perform addition
addition_result = cv2.add(image1, image2)

# Perform subtraction
subtraction_result = cv2.subtract(image1, image2)

# Show the results
cv2.imshow('Image 1', image1)
cv2.imshow('Image 2', image2)
cv2.imshow('Addition Result', addition_result)
cv2.imshow('Subtraction Result', subtraction_result)

# Save the results
cv2.imwrite('18add.jpg', addition_result)
cv2.imwrite('18sub.jpg', subtraction_result)

# Wait for a key press and then close all windows
cv2.waitKey(0)
cv2.destroyAllWindows()

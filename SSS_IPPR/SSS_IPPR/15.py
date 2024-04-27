import cv2

def apply_threshold(image, threshold_value):
    # Apply binary thresholding
    _, binary_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)
    return binary_image

# Load your grayscale image
gray_image = cv2.imread('15.jpg', cv2.IMREAD_GRAYSCALE)

# Set your threshold value
threshold_value = 127  # You can set this to any value between 0 and 255

# Apply threshold
binary_result = apply_threshold(gray_image, threshold_value)

# Display input grayscale image
cv2.imshow('Input Grayscale Image', gray_image)

# Display binary result
cv2.imshow('Binary Image', binary_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

# If you want to save the result
cv2.imwrite('15output.jpg', binary_result)

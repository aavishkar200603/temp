import cv2
import numpy as np

def edge_detection_sobel(rgb_image):
    # Convert the image to grayscale
    gray_image = cv2.cvtColor(rgb_image, cv2.COLOR_RGB2GRAY)
    
    # Apply Sobel operator in x and y directions
    sobel_x = cv2.Sobel(gray_image, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray_image, cv2.CV_64F, 0, 1, ksize=3)
    
    # Combine the results
    sobel_combined = cv2.addWeighted(cv2.convertScaleAbs(sobel_x), 0.5, 
                                     cv2.convertScaleAbs(sobel_y), 0.5, 0)
    
    # Apply threshold to get a binary image
    _, binary_image = cv2.threshold(sobel_combined, 50, 255, cv2.THRESH_BINARY)
    
    # Invert the binary image
    segmented_image = cv2.bitwise_not(binary_image)
    
    return segmented_image

# Read the input RGB image (replace 'input_rgb_image.jpg' with your image file)
rgb_image = cv2.imread("4.jpg")

# Perform edge detection using Sobel operator
segmented_image = edge_detection_sobel(rgb_image)

# Display the segmented image
cv2.imshow("Segmented Image", segmented_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Save the segmented image (replace 'output_segmented_image.jpg' with desired output filename)
cv2.imwrite("4output.jpg", segmented_image)

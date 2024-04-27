import cv2
import numpy as np

def negative_image(input_image):
    # Read the input image
    img = cv2.imread(input_image, cv2.IMREAD_GRAYSCALE)
    
    # Calculate the negative image
    negative_img = 255 - img
    
    # Display the original and negative images (optional)
    cv2.imshow('Original Image', img)
    cv2.imshow('Negative Image', negative_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    
    return negative_img

# Example usage
input_image_path = 'Original Image.jpg'
negative_result = negative_image(input_image_path)

# Save the negative image
cv2.imwrite('negative_image.jpg', negative_result)


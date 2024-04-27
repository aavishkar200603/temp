import cv2
import numpy as np

def normalize_image(image):
    # Convert image to float32 for calculations
    image_float = image.astype(np.float32)
    
    # Normalize to range [0, 1]
    normalized_image = image_float / 255.0
    
    # Ensure values are within valid range
    normalized_image = np.clip(normalized_image, 0, 1)
    
    # Convert back to uint8
    normalized_image_uint8 = (normalized_image * 255).astype(np.uint8)
    
    return normalized_image_uint8

# Load your 24-bit RGB image
rgb_image = cv2.imread('16.jpg', cv2.IMREAD_COLOR)

# Ensure the image is in RGB format
rgb_image = cv2.cvtColor(rgb_image, cv2.COLOR_BGR2RGB)

# Normalize the image
normalized_image = normalize_image(rgb_image)

# Display or save the result
cv2.imshow('Original RGB Image', rgb_image)
cv2.imshow('Normalized RGB Image', normalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# If you want to save the result
cv2.imwrite('16output.jpg', cv2.cvtColor(normalized_image, cv2.COLOR_RGB2BGR))

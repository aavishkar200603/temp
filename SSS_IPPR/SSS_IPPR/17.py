import cv2
import numpy as np
import matplotlib.pyplot as plt

def intensity_slicing_preserve_background(image, lower, upper):
    # Create a copy of the image to preserve the original
    result_image = np.copy(image)
    
    # Apply intensity slicing with background preservation
    result_image[(image >= lower) & (image <= upper)] = 255
    
    return result_image

def intensity_slicing_non_preserve_background(image, lower, upper):
    # Create a copy of the image to preserve the original
    result_image = np.copy(image)
    
    # Apply intensity slicing without background preservation
    result_image[(image >= lower) & (image <= upper)] = 0
    
    return result_image

# Read the input image (replace 'input_image.jpg' with your image file)
input_image = cv2.imread('17.jpg', cv2.IMREAD_GRAYSCALE)

# Define the intensity range for slicing (adjust as needed)
lower_intensity = 100
upper_intensity = 200

# Apply intensity slicing with preserving background
result_preserve_background = intensity_slicing_preserve_background(input_image, lower_intensity, upper_intensity)

# Apply intensity slicing without preserving background
result_non_preserve_background = intensity_slicing_non_preserve_background(input_image, lower_intensity, upper_intensity)

# Display the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(input_image, cv2.COLOR_BGR2RGB), cmap='gray')
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(result_preserve_background, cmap='gray')
plt.title('Intensity Slicing (Preserve Background)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(result_non_preserve_background, cmap='gray')
plt.title('Intensity Slicing (Non-Preserve Background)')
plt.axis('off')

plt.tight_layout()
plt.show()

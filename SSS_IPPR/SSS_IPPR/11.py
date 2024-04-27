import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('11.jpg')

# Get image dimensions
height, width = image.shape[:2]

# Define rotation angles (clockwise and anti-clockwise)
angle_cw = 90
angle_acw = -90

# Calculate rotation matrices
center = (width // 2, height // 2)
M_cw = cv2.getRotationMatrix2D(center, angle_cw, 1.0)
M_acw = cv2.getRotationMatrix2D(center, angle_acw, 1.0)

# Apply the rotation to the image
rotated_image_cw = cv2.warpAffine(image, M_cw, (width, height))
rotated_image_acw = cv2.warpAffine(image, M_acw, (width, height))

# Convert the rotated images to RGB for visualization
rotated_image_cw_rgb = cv2.cvtColor(rotated_image_cw, cv2.COLOR_BGR2RGB)
rotated_image_acw_rgb = cv2.cvtColor(rotated_image_acw, cv2.COLOR_BGR2RGB)

# Plot the images
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(rotated_image_cw_rgb)
plt.title('Rotated Clockwise (90 degrees)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(rotated_image_acw_rgb)
plt.title('Rotated Anti-Clockwise (90 degrees)')
plt.axis('off')

plt.tight_layout()
plt.show()

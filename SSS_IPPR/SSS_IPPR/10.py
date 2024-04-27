import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('10.jpg')

# Define translation matrices for rightward shift (20 units) and downward shift (10 units)
tx_right = 20
ty_down = 10

# Construct the translation matrices
M_right = np.float32([[1, 0, tx_right], [0, 1, 0]])
M_down = np.float32([[1, 0, 0], [0, 1, ty_down]])

# Apply the translation to the image
translated_image_right = cv2.warpAffine(image, M_right, (image.shape[1], image.shape[0]))
translated_image_down = cv2.warpAffine(image, M_down, (image.shape[1], image.shape[0]))

# Convert the translated images to RGB for visualization
translated_image_right_rgb = cv2.cvtColor(translated_image_right, cv2.COLOR_BGR2RGB)
translated_image_down_rgb = cv2.cvtColor(translated_image_down, cv2.COLOR_BGR2RGB)

# Plot the images
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(translated_image_right_rgb)
plt.title('Translated Right (20 units)')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(translated_image_down_rgb)
plt.title('Translated Down (10 units)')
plt.axis('off')

plt.tight_layout()
plt.show()

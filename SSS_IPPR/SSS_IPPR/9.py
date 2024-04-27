import cv2
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('9.jpg')

# Scale the image by a factor of 2
scaled_image_2x = cv2.resize(image, None, fx=2, fy=2, interpolation=cv2.INTER_LINEAR)

# Scale the image by a factor of 0.5
scaled_image_0_5x = cv2.resize(image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# Convert the scaled images to RGB for visualization
scaled_image_2x_rgb = cv2.cvtColor(scaled_image_2x, cv2.COLOR_BGR2RGB)
scaled_image_0_5x_rgb = cv2.cvtColor(scaled_image_0_5x, cv2.COLOR_BGR2RGB)

# Plot the images
plt.figure(figsize=(10, 6))

plt.subplot(1, 3, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 3, 2)
plt.imshow(scaled_image_2x_rgb)
plt.title('Scaled 2x')
plt.axis('off')

plt.subplot(1, 3, 3)
plt.imshow(scaled_image_0_5x_rgb)
plt.title('Scaled 0.5x')
plt.axis('off')

plt.tight_layout()
plt.show()

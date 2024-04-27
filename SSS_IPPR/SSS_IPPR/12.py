import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('12.jpg')

# Convert image to YCrCb color space (JPEG compression operates on Y channel)
image_ycrcb = cv2.cvtColor(image, cv2.COLOR_BGR2YCrCb)

# Apply JPEG compression
compression_quality = 50  # Set compression quality (0-100, higher is better quality)
compressed_image = cv2.imencode('.jpg', image_ycrcb, [int(cv2.IMWRITE_JPEG_QUALITY), compression_quality])[1]
decompressed_image_ycrcb = cv2.imdecode(compressed_image, cv2.IMREAD_COLOR)

# Convert the decompressed image back to BGR
decompressed_image = cv2.cvtColor(decompressed_image_ycrcb, cv2.COLOR_YCrCb2BGR)

# Calculate PSNR between original and decompressed images
psnr_value = cv2.PSNR(image, decompressed_image)

# Display the original and decompressed images
plt.figure(figsize=(10, 6))

plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(decompressed_image, cv2.COLOR_BGR2RGB))
plt.title('Decompressed Image (JPEG Quality: {})'.format(compression_quality))
plt.axis('off')

plt.tight_layout()
plt.show()

# Print the PSNR value
print("PSNR value:", psnr_value)

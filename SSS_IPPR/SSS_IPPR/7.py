import cv2
import numpy as np
import matplotlib.pyplot as plt

# Load the image
image = cv2.imread('7.jpg')

# Split the image into RGB channels
b, g, r = cv2.split(image)

# Compute histograms
histogram_b = cv2.calcHist([b], [0], None, [256], [0, 256])
histogram_g = cv2.calcHist([g], [0], None, [256], [0, 256])
histogram_r = cv2.calcHist([r], [0], None, [256], [0, 256])

# Plot the histograms
plt.figure(figsize=(8, 6))
plt.subplot(3, 1, 1)
plt.plot(histogram_b, color='b')
plt.title('Histogram - Blue Channel')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(3, 1, 2)
plt.plot(histogram_g, color='g')
plt.title('Histogram - Green Channel')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.subplot(3, 1, 3)
plt.plot(histogram_r, color='r')
plt.title('Histogram - Red Channel')
plt.xlabel('Pixel Intensity')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()

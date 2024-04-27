import cv2
import numpy as np

def enhance_color_channel(image, channel, enhancement_factor):
    """
    Enhances a specific color channel of an RGB image by multiplying with enhancement factor.

    Args:
        image: Input RGB image (24 bit).
        channel: Channel to enhance, should be 0 (for Red), 1 (for Green), or 2 (for Blue).
        enhancement_factor: Factor to multiply the chosen channel by.

    Returns:
        Enhanced RGB image.
    """
    # Split the image into its RGB channels
    b, g, r = cv2.split(image)

    # Apply enhancement to the selected channel
    if channel == 0:  # Red channel
        r = np.clip(r * enhancement_factor, 0, 255).astype(np.uint8)
    elif channel == 1:  # Green channel
        g = np.clip(g * enhancement_factor, 0, 255).astype(np.uint8)
    elif channel == 2:  # Blue channel
        b = np.clip(b * enhancement_factor, 0, 255).astype(np.uint8)

    # Merge the channels back together
    enhanced_image = cv2.merge((b, g, r))

    return enhanced_image

# Load an example image
image_path = "19.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Define enhancement parameters
    channel_to_enhance = 1  # Enhance the Green channel
    enhancement_factor = 1.5  # Multiply the Green channel by 1.5

    # Enhance the selected color channel
    enhanced_image = enhance_color_channel(image, channel_to_enhance, enhancement_factor)

    # Display original and enhanced images
    cv2.imshow("Original Image", image)
    cv2.imshow("Enhanced Image", enhanced_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the enhanced image
    cv2.imwrite("19output.jpg", enhanced_image)

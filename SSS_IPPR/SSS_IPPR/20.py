import cv2

def smooth_image(image, kernel_size):
    """
    Smoothens (or blurs) an RGB image using Gaussian blur.

    Args:
        image: Input RGB image (24 bit).
        kernel_size: Size of the Gaussian kernel (should be an odd number, e.g., 3, 5, 7).

    Returns:
        Smoothed RGB image.
    """
    smoothed_image = cv2.GaussianBlur(image, (kernel_size, kernel_size), 0)
    return smoothed_image

# Load an example noisy image
image_path = "20.jpg"
image = cv2.imread(image_path)

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found.")
else:
    # Define the size of the Gaussian kernel (odd number)
    kernel_size = 5

    # Smooth the image
    smoothed_image = smooth_image(image, kernel_size)

    # Display original and smoothed images
    cv2.imshow("Original Noisy Image", image)
    cv2.imshow("Smoothed Image", smoothed_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the smoothed image
    cv2.imwrite("20output.jpg", smoothed_image)

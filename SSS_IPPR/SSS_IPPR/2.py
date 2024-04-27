import cv2

def negative_image(image_path):
    # Load the image
    image = cv2.imread(image_path)

    # Check if image was loaded
    if image is None:
        print("Error: Could not read the image.")
        return

    # Invert each pixel's color
    negative_image = 255 - image

    # Display original and negative images (optional)
    cv2.imshow("Original Image", image)
    cv2.imshow("Negative Image", negative_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Save the negative image
    negative_image_path = "negative_" + image_path
    cv2.imwrite(negative_image_path, negative_image)

    print("Negative image saved as:", negative_image_path)

# Provide the path to your 24-bit color image
image_path = "2.jpg"
negative_image(image_path)

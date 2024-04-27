from PIL import Image

def rgb_to_cmy(rgb_image):
    # Ensure the image is in RGB mode
    rgb_image = rgb_image.convert("RGB")
    
    # Create a new blank image for CMY
    cmy_image = Image.new("RGB", rgb_image.size)
    
    # Get the width and height of the image
    width, height = rgb_image.size
    
    # Iterate through each pixel
    for x in range(width):
        for y in range(height):
            # Get RGB values of the pixel
            r, g, b = rgb_image.getpixel((x, y))
            
            # Convert to CMY
            c = 255 - r
            m = 255 - g
            y_val = 255 - b  # Renamed to avoid conflict with loop variable y
            
            # Set CMY values in the new image
            cmy_image.putpixel((x, y), (c, m, y_val))
    
    return cmy_image

# Open an RGB image (replace 'input_rgb_image.jpg' with your image file)
rgb_image = Image.open("3.jpg")

# Convert RGB to CMY
cmy_image = rgb_to_cmy(rgb_image)

# Save or display the CMY image (replace 'output_cmy_image.jpg' with desired output filename)
cmy_image.save("3output.jpg")
cmy_image.show()

import sys
from PIL import Image
import os

def resize_crop_image(input_image, target_size):
    image = Image.open(input_image)
    image = image.resize(target_size)
    return image

def overlay_shirt(input_image, output_image, shirt_image, y_offset):
    input_size = input_image.size
    shirt_size = shirt_image.size

    if input_size != shirt_size:
        shirt_image = resize_crop_image(shirt_image, input_size)

    # Convert images to RGBA mode
    input_image = input_image.convert('RGBA')
    shirt_image = shirt_image.convert('RGBA')

    # Calculate the position to overlay the shirt (centered horizontally)
    x_offset = (input_size[0] - shirt_size[0]) // 2  # Center the shirt horizontally

    # Adjust the vertical position of the shirt
    y_offset = -y_offset  # Negative value moves the shirt up

    # Create a new transparent image to hold the overlay
    overlay = Image.new('RGBA', input_size, (0, 0, 0, 0))
    overlay.paste(shirt_image, (x_offset, y_offset))

    # Composite the overlay on the input image
    result_image = Image.alpha_composite(input_image, overlay)

    # Convert the result image to RGB mode if saving as JPEG
    if determine_output_format(output_image) == 'JPEG':
        result_image = result_image.convert('RGB')

    # Save the result image to the output file
    result_image.save(output_image, format=determine_output_format(output_image))

def determine_output_format(output_image_path):
    _, file_extension = os.path.splitext(output_image_path)
    if file_extension.lower() == '.jpg' or file_extension.lower() == '.jpeg':
        return 'JPEG'
    elif file_extension.lower() == '.png':
        return 'PNG'
    else:
        raise ValueError("Unsupported output image format. Please use JPG or PNG.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python shirt.py before1.jpg after1.jpg")
        sys.exit(1)

    input_image_path = sys.argv[1]
    output_image_path = sys.argv[2]

    try:
        # Load the "shirt.png" image
        shirt_image = Image.open("shirt.png")

        # Set the desired uplift value (change this to uplift or lower the shirt)
        uplift_amount = 50

        # Resize, crop, and overlay the images with the uplift amount
        overlay_shirt(resize_crop_image(input_image_path, shirt_image.size), output_image_path, shirt_image, uplift_amount)
        print("Image processing complete.")
    except FileNotFoundError:
        print("File Not Found :(")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", e)




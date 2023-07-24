import sys
from PIL import Image
import os

def resize_crop_image(input_image, target_size):
    image = Image.open(input_image)
    image = image.resize(target_size)
    return image

def overlay_shirt(input_image, output_image, shirt_image):
    input_size = input_image.size
    shirt_size = shirt_image.size
    if input_size != shirt_size:
        shirt_image = resize_crop_image(shirt_image, input_size)

    # Convert images to RGBA mode
    input_image = input_image.convert('RGBA')
    shirt_image = shirt_image.convert('RGBA')

    # Overlay the shirt on the input image
    result_image = Image.alpha_composite(input_image, shirt_image)

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

        # Resize, crop, and overlay the images
        overlay_shirt(resize_crop_image(input_image_path, shirt_image.size), output_image_path, shirt_image)
        print("Image processing complete.")
    except FileNotFoundError:
        print("File Not Found :(")
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print("An error occurred:", e)


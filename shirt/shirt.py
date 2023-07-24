import sys
from PIL import Image

def resize_crop_image(input_image, target_size):
    image = Image.open(input_image)
    image = image.resize(target_size)
    return image

def overlay_shirt(input_image, output_image, shirt_image):
    input_size = input_image.size
    shirt_size = shirt_image.size
    if input_size != shirt_size:
        shirt_image = resize_crop_image(shirt_image, input_size)

    # Overlay the shirt on the input image
    result_image = Image.alpha_composite(input_image.convert('RGBA'), shirt_image)

    # Save the result image to the output file
    result_image.save(output_image)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python shirt.py input_image.jpg output_image.jpg")
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
    except Exception as e:
        print("An error occurred:", e)

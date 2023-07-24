import sys
import os
import csv
from PIL import Image

before_image_path = sys.argv[1]
after_image_path = sys.argv[2]

before_image_base_name, before_image_extension = os.path.splitext(before_image_path)
after_image_base_name, after_image_extension = os.path.splitext(after_image_path)


def editing_image(input_image, output_image):
    try:
        image = Image.open(input_image)

    except FileNotFoundError:
        print("File Not Found :(")










if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py beforeimage.jpg afterimage.jpg or afterimage.png")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]
    editing_image(input_image, output_image)
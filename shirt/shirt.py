import sys
import os
from PIL import Image


def editing_image(input_image, output_image):
    try:
        shirt = Image.open('shirt.png')
        inputimage = Image.open(input_image)
        outputimage = Image.open(output_image)

        # size = shirt.size

        outputimage.paste(shirt, inputimage)
    except FileNotFoundError:
        print("File Not Found :(")










if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py beforeimage.jpg afterimage.jpg or afterimage.png")
        sys.exit(1)

    input_image = sys.argv[1]
    output_image = sys.argv[2]
    editing_image(input_image, output_image)
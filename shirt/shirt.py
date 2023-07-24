import sys
import os
import csv
from PIL import Image

input_path = sys.argv[1]
output_path = sys.argv[2]
base_name, file_extension


def editing_image(input_image, output_image):











if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script_name.py beforeimage.jpg afterimage.jpg or afterimage.png")
        sys.exit(1)
    input_image = sys.argv[1]
    output_image = sys.argv[2]
    editing_image(input_image, output_image)
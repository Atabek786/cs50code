import sys
import random

# Define the available fonts
available_fonts = [
    "standard",
    "banner",
    "slant",
    "big",
    "small",
    # Add more fonts here
]

def print_random_font(text):
    # Choose a random font
    font = random.choice(available_fonts)
    print_text_in_font(text, font)

def print_text_in_font(text, font):
    # Load the font file
    try:
        with open(f"fonts/{font}.txt", "r") as file:
            font_data = file.read().splitlines()
    except FileNotFoundError:
        print(f"Font '{font}' not found.")
        return

    # Print each line of the text in the chosen font
    for line in font_data:
        formatted_line = ""
        for char in text:
            if ord(char) < 32 or ord(char) > 126:
                formatted_line += " "  # Skip non-printable characters
            else:
                index = ord(char) - 32
                if index >= len(line):
                    formatted_line += " "  # Skip unsupported characters
                else:
                    formatted_line += line[index]
        print(formatted_line)

# Check command-line arguments
if len(sys.argv) == 1:
    # No arguments, output text in a random font
    text = input("Enter the text to print: ")
    print_random_font(text)
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    # Two arguments, output text in the specified font
    font = sys.argv[2]
    text = input("Enter the text to print: ")
    print_text_in_font(text, font)
else:
    print("Invalid arguments. Usage: python figlet.py [-f/--font FONT_NAME]")

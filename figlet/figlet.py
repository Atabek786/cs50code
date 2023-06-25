import sys
import figlet


# Check command-line arguments
if len(sys.argv) == 1:
    # No arguments, output text in a random font
    text = input("Enter the text to print: ")
    fonts = figlet.Fonts().getFonts()
    font = fonts[0] if fonts else None
    print_text_in_font(text, font)
elif len(sys.argv) == 3 and sys.argv[1] in ("-f", "--font"):
    # Two arguments, output text in the specified font
    font = sys.argv[2]
    text = input("Enter the text to print: ")
    print_text_in_font(text, font)
else:
    print("Invalid arguments. Usage: python figlet.py [-f/--font FONT_NAME]")

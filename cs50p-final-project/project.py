import os
import json
from pathlib import Path

import openai
def main():
    userprompt = input("Type text that will transform into an image: ")
    DATA_DIR = Path.cwd() / "responses"

    DATA_DIR.mkdir(exist_ok=True)

    openai.api_key = os.getenv("OPENAI_API_KEY")

    response = openai.Image.create(
        prompt=userprompt,
        n=1,
        size="512x512",
        response_format="b64_json",
    )

    file_name = DATA_DIR / f"{userprompt[:5]}-{response['created']}.json"

    with open(file_name, mode="w", encoding="utf-8") as file:
        json.dump(response, file)




































def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        return 0
    elif greeting.startswith("h"):
        return 20
    else:
        return 100

def convert(fraction):
    while True:
        try:
            # Try to split the fuel
            numerator, denominator = fraction.split("/")
            # Convert into integers
            new_numerator = int(numerator)
            new_denominator = int(denominator)
            # Calculate the percentage
            f = new_numerator / new_denominator
            # Check if its less than 1 and stop the loop
            if f <= 1:
                # Multiply percentage by 100
                p = int(f * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError,ZeroDivisionError):
            raise

def gauge(percentage):
    # Check if percentage is less than 1, return E
    if percentage <= 1:
        return "E"
    # Check if percentage is greater than 99, return F
    elif percentage >= 99:
        return "F"
    # Otherwise, return the %
    else:
        return str(percentage) + "%"

if __name__ == "__main__":
    main()
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







def hello(s):
    if s.startswith("hello"):
        return 0

def h(s)
    if s.startswith("h"):
        return 20
def other(s):
    if not s.startswith("h"):
        return 100


if __name__ == "__main__":
    main()
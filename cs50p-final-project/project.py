import os
import openai

userprompt = input("Type text that will transform into an image: ")

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.Image.create(
    prompt=userprompt,
    n=1
    size="256x256"
    response_format="b64_json",
)

print(response["data"][0]["b64_json"][:50])

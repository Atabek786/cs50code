# TextIntoImage AI
#### Video Demo:  <URL HERE>
#### Description:
TextIntoImage AI is a Python project that harnesses the power of the OpenAI API to convert text prompts into captivating images and generate variations of existing images. This project demonstrates how to interact with the OpenAI API to create visual representations based on textual input.

## Features:

1. **Text-to-Image Conversion:** Utilizing the `main()` function, users can input a text prompt, which the OpenAI API transforms into an image. The resulting image is then saved in JSON format, accompanied by relevant metadata.

2. **Image Variation Generation:** The project includes the `openai.Image.create_variation()` function, allowing users to take an existing image stored in the "responses" directory and generate multiple image variations. These variations are also saved in JSON format for future use.

## Requirements:

To run this project, ensure the following prerequisites are met:

- Python is installed on your system.
- The necessary libraries specified in the Python script are installed (`openai`, `os`, `json`, `base64`, and `pathlib`).
- An OpenAI API key is required. Set it as an environment variable with the name `OPENAI_API_KEY` to access the OpenAI API for image-related tasks.

## How to Use:

1. Clone this repository to your local machine.

2. Install the required Python libraries by running the following command in your terminal or command prompt:  pip install openai

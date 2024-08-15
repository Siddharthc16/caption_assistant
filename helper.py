import os
from dotenv import load_dotenv
import base64
import requests
from prompt import Prompt
load_dotenv()


class CaptionHelper(Prompt):
    """Helper class for generating captions."""

    def _encode_image_to_base64(self, image_path):
        """Encodes the image at the given path to a base64 string."""
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

    # Function to generate captions using OpenAI API
    def generate_captions(self, image_path, memories):
        """Generates captions for an image using the OpenAI API."""
        # Encode the image to base64
        base64_image = self._encode_image_to_base64(image_path)

        # Set up headers for the OpenAI API request
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {os.getenv('OPENAI_API_KEY')}"
        }

        # Prepare the payload with the image and prompt
        payload = {
            "model": "gpt-4o-mini",
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": self.get_prompt(memories)
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            }
                        }
                    ]
                }
            ],
            "max_tokens": 500
        }

        # Make the API request to OpenAI
        response = requests.post(
            "https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

        # Check if the response is successful
        if response.status_code == 200:
            # Extract and return the captions
            captions = response.json()['choices'][0]['message']['content']
            return captions
        
        raise Exception(
                f"Failed to generate captions: {response.status_code} - {response.text}")

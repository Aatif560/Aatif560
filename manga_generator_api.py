import requests
import io
from PIL import Image
import os

# You can get a free token from https://huggingface.co/settings/tokens
# For this script to work, set the HUGGING_FACE_TOKEN environment variable.
HUGGING_FACE_TOKEN = os.environ.get("HUGGING_FACE_TOKEN", "YOUR_HF_TOKEN_HERE")

# Using a good anime/manga style model available on Hugging Face Inference API
# e.g., andite/anything-v4.0 or prompthero/openjourney or cagliostrolab/animagine-xl-3.1
API_URL = "https://api-inference.huggingface.co/models/cagliostrolab/animagine-xl-3.1"
HEADERS = {"Authorization": f"Bearer {HUGGING_FACE_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=HEADERS, json=payload)
    if response.status_code != 200:
        print(f"Error: {response.status_code} - {response.text}")
        return None
    return response.content

def main():
    print("Welcome to Manga Image Generator (API Version)!")
    print("This version is recommended for your i5 6th gen + 8GB RAM PC, as it uses the cloud.")
    print("---------------------------------------------------------")

    user_prompt = input("Enter your prompt for the image: ")

    # Adding quality tags and style tags for detailed color manga
    enhanced_prompt = f"masterpiece, best quality, detailed, full color, manga style, anime style, {user_prompt}"
    negative_prompt = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"

    print(f"\nGenerating image with enhanced prompt: '{enhanced_prompt}'")
    print("Please wait...")

    image_bytes = query({
        "inputs": enhanced_prompt,
        "parameters": {
            "negative_prompt": negative_prompt,
        }
    })

    if image_bytes:
        try:
            image = Image.open(io.BytesIO(image_bytes))
            output_filename = "generated_manga_api.png"
            image.save(output_filename)
            print(f"\nSuccess! Image saved as {output_filename}")
            # Try to show the image if possible
            image.show()
        except Exception as e:
            print(f"Failed to process image: {e}")

if __name__ == "__main__":
    main()

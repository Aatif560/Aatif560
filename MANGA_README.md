# Manga Image Generator

Yes, it is definitely possible to create a program where you input a prompt and it gives you a detailed, colored manga-style image!

However, because you are running an **Intel i5 6th Gen CPU with 8GB RAM and no dedicated GPU**, generating these images *locally* on your own machine will be very difficult, slow, and may crash due to running out of RAM.

To solve this, I have provided **two options**:

## Option 1: The API Method (Highly Recommended)
This uses the free Hugging Face API to generate the image on their powerful cloud servers and send it back to your PC.
- **Speed:** Fast (usually takes a few seconds).
- **RAM/CPU Usage:** Very low (your PC just sends text and receives a picture).
- **File:** `manga_generator_api.py`

### How to use Option 1:
1. Create a free account at [Hugging Face](https://huggingface.co/).
2. Go to your settings and create an Access Token: [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens).
3. Set your token as an environment variable in your terminal:
   - On Windows: `set HUGGING_FACE_TOKEN=your_token_here`
   - On Linux/Mac: `export HUGGING_FACE_TOKEN=your_token_here`
4. Install requirements: `pip install -r requirements.txt`
5. Run the script: `python manga_generator_api.py`
6. Type your prompt (e.g., "a young ninja standing on a cliff"). The script automatically adds tags to make it detailed, colored, and manga style!

## Option 2: The Local Method (Use with caution)
This runs the AI model directly on your CPU.
- **Speed:** Extremely slow (can take 15-30+ minutes per image on an i5 6th Gen).
- **RAM/CPU Usage:** Very high. It will max out your 8GB RAM. You MUST close all other programs (browsers, background apps) before running this, or your PC will freeze/crash.
- **File:** `manga_generator_local.py`

### How to use Option 2:
1. Install requirements: `pip install -r requirements.txt`
2. Run the script: `python manga_generator_local.py`
3. The first time you run it, it will download several gigabytes of model files.
4. Type your prompt and wait patiently.

## Prompting Tips for Manga Style
The scripts automatically enhance your prompt with keywords like `masterpiece, best quality, detailed, full color, manga style, anime style`.
When you type your prompt, focus on describing the scene, characters, and lighting.
For example: `a young woman reading a book in a cozy magical library, sunlight streaming through stained glass windows`

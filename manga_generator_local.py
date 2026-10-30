import torch
from diffusers import StableDiffusionPipeline
import os

def main():
    print("Welcome to Manga Image Generator (Local CPU Version)!")
    print("WARNING: You are running this on an Intel i5 6th gen with 8GB RAM using CPU only.")
    print("This will take a VERY LONG TIME (potentially 15-30+ minutes per image).")
    print("It might also crash if it runs out of RAM. Ensure all other applications are closed.")
    print("---------------------------------------------------------")

    # We use a standard 1.5 model fine-tuned for anime/manga to save some RAM
    # compared to SDXL models.
    model_id = "andite/anything-v4.0"

    print(f"Loading model '{model_id}'...")
    print("This will take a few minutes and download several gigabytes if run for the first time.")

    try:
        # Load the pipeline. We must use float32 for CPU.
        pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32,
            safety_checker=None # Disabling safety checker to save RAM
        )

        # Move to CPU
        pipe = pipe.to("cpu")

        # Memory optimization for 8GB RAM
        # We cannot use xformers on CPU, but we can try to use attention slicing
        pipe.enable_attention_slicing()

        print("\nModel loaded successfully!")

        user_prompt = input("Enter your prompt for the image: ")

        # Enhancing for detailed color manga
        enhanced_prompt = f"masterpiece, best quality, detailed, full color, manga style, anime style, {user_prompt}"
        negative_prompt = "lowres, bad anatomy, bad hands, text, error, missing fingers, extra digit, fewer digits, cropped, worst quality, low quality, normal quality, jpeg artifacts, signature, watermark, username, blurry"

        print(f"\nGenerating image with enhanced prompt: '{enhanced_prompt}'")
        print("Starting generation... Go grab a coffee, this will take a while!")

        # Generate image
        # Reducing inference steps and resolution to make it survive on 8GB RAM / older CPU
        image = pipe(
            prompt=enhanced_prompt,
            negative_prompt=negative_prompt,
            num_inference_steps=20, # Reduced from 50 to save time
            height=512, # Keep at 512x512 to avoid out of memory
            width=512
        ).images[0]

        output_filename = "generated_manga_local.png"
        image.save(output_filename)
        print(f"\nSuccess! Image saved as {output_filename}")

    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("If the error is about memory (OOM or Killed), your PC does not have enough RAM to run this locally.")
        print("Please use the API version (manga_generator_api.py) instead.")

if __name__ == "__main__":
    main()

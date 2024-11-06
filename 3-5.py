import torch
from diffusers import StableDiffusion3Pipeline

# Define the model name
large_model = "stabilityai/stable-diffusion-3.5-large"

# Initialize the Stable Diffusion pipeline with the large model
# Load the model with reduced precision (bfloat16) for better memory efficiency
pipe = StableDiffusion3Pipeline.from_pretrained(large_model, torch_dtype=torch.bfloat16)

# Enable attention slicing to reduce memory usage, helpful for high-resolution images
pipe.enable_attention_slicing()

# Move the pipeline to the GPU to speed up inference
pipe = pipe.to("cuda")

# Define the prompt for image generation
prompt = "a programmer touching grass"

# Generate images based on the prompt with specified inference settings
results = pipe(
    prompt,
    num_inference_steps=20,  # Number of diffusion steps, higher values increase quality
    guidance_scale=3.5,      # Higher values increase adherence to the prompt
    height=512,              # Height of the output image in pixels
    width=512                # Width of the output image in pixels
)

# Retrieve the generated images from the results
images = results.images

# Save each generated image with a unique filename
for i, img in enumerate(images):
    img.save(f"image_{i}.png")  # Save each image with a unique name



import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler

# Define the model name for the smaller version of Stable Diffusion
small_model = "stabilityai/stable-diffusion-2-1"

# Initialize the Stable Diffusion pipeline with the smaller model
# Load the model using bfloat16 precision for optimized memory usage
pipe = StableDiffusionPipeline.from_pretrained(small_model, torch_dtype=torch.bfloat16)

# Replace the default scheduler with DPMSolverMultistepScheduler for better generation quality
pipe.scheduler = DPMSolverMultistepScheduler.from_config(pipe.scheduler.config)

# Enable attention slicing to reduce memory usage during inference
pipe.enable_attention_slicing()

# Move the pipeline to GPU for faster computation
pipe = pipe.to("cuda")

# Define a list of prompts for image generation
prompts = [
    "a programmer touching grass",
    "A dreamlike landscape with floating islands and waterfalls under a starry sky.",
    "A Roman soldier standing guard in front of the Colosseum during sunset.",
    "A cyberpunk character with neon tattoos in a rain-soaked alley."
]

# Generate images based on the prompts with specified settings
results = pipe(
    prompts,
    num_inference_steps=50,  # Number of diffusion steps for higher quality output
    guidance_scale=3.5,      # Controls how closely the image matches the prompt
    height=512,              # Height of the output image in pixels
    width=512                # Width of the output image in pixels
)

# Retrieve the generated images from the results
images = results.images

# Save each generated image with a unique filename
for i, img in enumerate(images):
    img.save(f"image_{i}.png")  # Save each image with a unique name



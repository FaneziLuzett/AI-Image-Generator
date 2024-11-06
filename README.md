Running on Google Colab

    Access the Colab Notebook
    Open the Google Colab notebook by clicking on this link: Notebook Link

    Enable GPU for Better Performance
        In the Colab menu, select Runtime -> Change runtime type.
        Choose GPU as the hardware accelerator, and select the T4 option.

    Execute Code Cells
    Run the cells sequentially to start generating images.

Running Locally

To run the program locally, follow these instructions:
1. Ensure Python is Installed

Make sure Python is installed on your system. Download Python if needed.
2. Set Up CUDA (For NVIDIA GPUs)

If your machine has an NVIDIA GPU, install CUDA for enhanced performance by following the guide on NVIDIA's CUDA Toolkit page.
3. Create and Activate a Virtual Environment

    Create a virtual environment by running:

    python -m venv myenv

    Activate it:
        Linux/macOS: source myenv/bin/activate
        Windows: myenv\Scripts\activate

4. Clone the Repository and Install Dependencies

    Clone this repository:

git clone <repository-url>

Navigate to the project directory and install required packages:

    cd <repository-directory>
    pip install -r requirements.txt

5. Install PyTorch

Install PyTorch based on your system specifications by following the instructions at PyTorch’s website.
6. Set Up a Hugging Face Account and Access Token

    Create an Account
    Sign up at Hugging Face.

    Generate Access Token
    After logging in, go to your account settings and generate an access token.

    Login to Hugging Face CLI
    Run:

    huggingface-cli login

    Paste your access token when prompted.

    Request Access to High-End Models
    Some models require you to accept their license. For instance, if you plan to use the Stable Diffusion 3.5 model, you’ll need to accept the license here.

7. Select and Run a Script

Choose the appropriate script based on your hardware:

    2-1.py: Suitable for most configurations.
    3-5.py: For advanced GPUs only; this option takes significantly longer to process.
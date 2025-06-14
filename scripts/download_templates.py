import os
import requests
from pathlib import Path

# Create directories if they don't exist
data_dir = Path(__file__).parent.parent / "data"
images_dir = data_dir / "images"
images_dir.mkdir(parents=True, exist_ok=True)

# Template URLs
templates = {
    "drake.jpg": "https://raw.githubusercontent.com/rahil-p/meme-generator/main/templates/drake.jpg",
    "doge.jpg": "https://raw.githubusercontent.com/rahil-p/meme-generator/main/templates/doge.jpg",
    "success.jpg": "https://raw.githubusercontent.com/rahil-p/meme-generator/main/templates/success.jpg"
}

def download_image(url: str, filename: str):
    """Download image from URL and save to file."""
    response = requests.get(url)
    if response.status_code == 200:
        with open(images_dir / filename, "wb") as f:
            f.write(response.content)
        print(f"Downloaded {filename}")
    else:
        print(f"Failed to download {filename}")

# Download templates
for filename, url in templates.items():
    if not (images_dir / filename).exists():
        download_image(url, filename)
    else:
        print(f"Skipping {filename} - already exists")

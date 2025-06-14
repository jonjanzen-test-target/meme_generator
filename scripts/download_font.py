import os
from pathlib import Path
import requests

# Create font directory if it doesn't exist
fonts_dir = Path(__file__).parent.parent / "data" / "fonts"
fonts_dir.mkdir(parents=True, exist_ok=True)

# Use OpenSans-Bold as our meme font (reliably available)
font_url = "https://github.com/google/fonts/raw/main/ofl/opensans/static/OpenSans-Bold.ttf"

# Download Impact font (using Roboto Bold as a substitute since Impact isn't freely available)
font_path = fonts_dir / "impact.ttf"
if not font_path.exists():
    print(f"Downloading font to {font_path}")
    response = requests.get(impact_url)
    if response.status_code == 200:
        with open(font_path, "wb") as f:
            f.write(response.content)
        print("Font downloaded successfully")
    else:
        print("Failed to download font")

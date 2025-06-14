from pathlib import Path

# Project root directory
ROOT_DIR = Path(__file__).parent.parent

# Data directories
DATA_DIR = ROOT_DIR / "data"
IMAGES_DIR = DATA_DIR / "images"
FONTS_DIR = DATA_DIR / "fonts"

# Default settings
DEFAULT_FONT_SIZE = 50
DEFAULT_FONT = str(FONTS_DIR / "impact.ttf")  # You'll need to add this font
DEFAULT_TEXT_COLOR = "white"
DEFAULT_STROKE_COLOR = "black"
DEFAULT_STROKE_WIDTH = 2

# Image settings
MAX_IMAGE_SIZE = (800, 800)  # Maximum dimensions for generated memes
JPEG_QUALITY = 95  # Output quality for JPEG images

# Cache settings
ENABLE_CACHE = True
CACHE_DIR = ROOT_DIR / ".cache"

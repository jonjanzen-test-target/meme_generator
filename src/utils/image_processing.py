from PIL import Image, ImageDraw, ImageFont
import os
from typing import Tuple, Optional
from ..config import (
    DEFAULT_FONT_SIZE,
    DEFAULT_FONT,
    DEFAULT_TEXT_COLOR,
    DEFAULT_STROKE_COLOR,
    DEFAULT_STROKE_WIDTH,
    MAX_IMAGE_SIZE
)

def load_image(image_path: str) -> Image.Image:
    """Load and validate an image file."""
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"Image file not found: {image_path}")
    
    print(f"Loading image from: {image_path}")
    print(f"File size: {os.path.getsize(image_path)} bytes")
    
    try:
        image = Image.open(image_path)
        print(f"Image format: {image.format}")
        print(f"Image size: {image.size}")
        print(f"Image mode: {image.mode}")
        
        if image.mode != 'RGB':
            print(f"Converting image from {image.mode} to RGB")
            image = image.convert('RGB')
        return image
    except Exception as e:
        print(f"Error details: {str(e)}")
        raise

def resize_image(image: Image.Image, max_size: Tuple[int, int] = MAX_IMAGE_SIZE) -> Image.Image:
    """Resize image while maintaining aspect ratio."""
    if image.size[0] > max_size[0] or image.size[1] > max_size[1]:
        image.thumbnail(max_size, Image.Resampling.LANCZOS)
    return image

def calculate_font_size(
    image: Image.Image,
    text: str,
    max_width_ratio: float,
    initial_size_ratio: float,
    font_path: str
) -> int:
    """Calculate the optimal font size for the text to fit the image width."""
    target_width = int(image.width * max_width_ratio)
    initial_size = int(image.height * initial_size_ratio)
    
    try:
        font = ImageFont.truetype(font_path, initial_size)
    except OSError:
        font = ImageFont.load_default()
        return DEFAULT_FONT_SIZE
        
    text_bbox = font.getbbox(text)
    if not text_bbox:
        return initial_size
        
    text_width = text_bbox[2] - text_bbox[0]
    
    if text_width == 0:
        return initial_size
        
    # Scale font size to fit target width
    scaling_factor = target_width / text_width
    return int(initial_size * scaling_factor)

def add_text_to_image(
    image: Image.Image,
    text: str,
    position: Tuple[float, float],  # Position as ratios (0.0 to 1.0)
    max_width_ratio: float = 0.9,
    initial_size_ratio: float = 0.1,
    font_path: str = DEFAULT_FONT,
    text_color: str = DEFAULT_TEXT_COLOR,
    stroke_color: str = DEFAULT_STROKE_COLOR,
    stroke_width: int = DEFAULT_STROKE_WIDTH
) -> Image.Image:
    """Add text to an image with automatic sizing and positioning."""
    if not text:
        return image
        
    draw = ImageDraw.Draw(image)
    
    # Calculate font size
    font_size = calculate_font_size(
        image, text, max_width_ratio, initial_size_ratio, font_path
    )
    
    try:
        print(f"Attempting to load font from {font_path}")
        print(f"Font file exists: {os.path.exists(font_path)}")
        print(f"Font file size: {os.path.getsize(font_path)} bytes")
        font = ImageFont.truetype(font_path, font_size)
    except Exception as e:
        print(f"Error loading font: {str(e)}")
        font = ImageFont.load_default()
        print(f"Warning: Could not load font {font_path}, using default font")
    
    # Get text size for centering
    text_bbox = font.getbbox(text)
    if text_bbox:
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
        
        # Calculate absolute position (centered)
        x = int(position[0] * image.width - text_width / 2)
        y = int(position[1] * image.height - text_height / 2)
        
        # Draw the text with stroke
        draw.text(
            (x, y),
            text,
            font=font,
            fill=text_color,
            stroke_width=stroke_width,
            stroke_fill=stroke_color
        )
    
    return image

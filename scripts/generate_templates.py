from PIL import Image, ImageDraw
import os
from pathlib import Path

# Create directories if they don't exist
data_dir = Path(__file__).parent.parent / "data"
images_dir = data_dir / "images"
images_dir.mkdir(parents=True, exist_ok=True)

def create_template(filename: str, size=(800, 800), color="white"):
    """Create a basic template image with the specified color."""
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    print(f"Creating template {filename} in {images_dir}")
    
    # Add some basic visual elements based on the template type
    if "drake" in filename:
        # Drake template - split into two panels with gradient backgrounds
        for y in range(int(size[1]/2)):
            # Top panel - warm gradient
            color_top = int(200 + (55 * y/(size[1]/2)))
            draw.line([(0, y), (size[0], y)], 
                     fill=(color_top, int(color_top*0.8), int(color_top*0.6)))
            
            # Bottom panel - cool gradient
            y2 = y + int(size[1]/2)
            color_bottom = int(220 + (35 * y/(size[1]/2)))
            draw.line([(0, y2), (size[0], y2)], 
                     fill=(int(color_bottom*0.7), int(color_bottom*0.8), color_bottom))
            
        # Add panel divider
        draw.line([(0, size[1]/2), (size[0], size[1]/2)], fill="black", width=3)
        
    elif "doge" in filename:
        # Doge template - radial gradient with warm colors
        center = (size[0]/2, size[1]/2)
        max_dist = (size[0]**2 + size[1]**2)**0.5 / 2
        
        for y in range(size[1]):
            for x in range(0, size[0], 2):  # Skip every other pixel for performance
                dist = ((x - center[0])**2 + (y - center[1])**2)**0.5
                ratio = 1 - (dist / max_dist)
                r = int(255 * ratio)
                g = int(220 * ratio)
                b = int(180 * ratio)
                draw.point([(x, y), (x+1, y)], fill=(r, g, b))
                
    elif "success" in filename:
        # Success template - diagonal gradient with vibrant colors
        for y in range(size[1]):
            for x in range(0, size[0], 2):  # Skip every other pixel for performance
                ratio = (x + y) / (size[0] + size[1])
                r = int(100 + (155 * ratio))
                g = int(200 + (55 * ratio))
                b = int(100 + (155 * (1-ratio)))
                draw.point([(x, y), (x+1, y)], fill=(r, g, b))
    
    # Save the template
    img.save(images_dir / filename)
    print(f"Created template: {filename}")

# Create templates
templates = ["drake.jpg", "doge.jpg", "success.jpg"]
for template in templates:
    create_template(template)

from typing import Tuple, Optional, Dict
from PIL import Image
import os

from .utils.image_processing import load_image, resize_image, add_text_to_image
from .config import (
    IMAGES_DIR,
    MAX_IMAGE_SIZE,
    DEFAULT_FONT_SIZE,
    JPEG_QUALITY
)

from typing import Dict, List, Optional, Union
import os

from PIL import Image

from .config import IMAGES_DIR, MAX_IMAGE_SIZE, JPEG_QUALITY
from .utils.image_processing import load_image, resize_image, add_text_to_image
from .templates.meme_templates import TEMPLATES, MemeTemplate
from .ml.text_analyzer import TextAnalyzer

class MemeGenerator:
    def __init__(self):
        """Initialize the meme generator."""
        self.templates_cache: Dict[str, Image.Image] = {}
        self.text_analyzer = TextAnalyzer()
        
    def list_templates(self) -> List[str]:
        """List available meme templates."""
        return list(TEMPLATES.keys())
        
    def get_template_info(self, template_id: str) -> Optional[MemeTemplate]:
        """Get information about a specific template."""
        return TEMPLATES.get(template_id)
    
    def load_template(self, template_id: str) -> Image.Image:
        """Load a meme template from the templates directory."""
        if template_id in self.templates_cache:
            return self.templates_cache[template_id].copy()
        
        template = TEMPLATES.get(template_id)
        if not template:
            raise ValueError(f"Unknown template: {template_id}")
            
        template_path = os.path.join(IMAGES_DIR, template.filename)
        image = load_image(template_path)
        image = resize_image(image, MAX_IMAGE_SIZE)
        self.templates_cache[template_id] = image
        return image.copy()
    
    def create_meme(
        self,
        template_id: str,
        texts: Union[List[str], str],
        output_path: Optional[str] = None,
        use_ml: bool = True
    ) -> Image.Image:
        """Create a meme with the specified template and texts.
        
        Args:
            template_id: The ID of the template to use
            texts: Either a list of texts (one per position) or a string (split into top/bottom)
            output_path: Optional path to save the meme
            use_ml: Whether to use ML for optimization (default: True)
        """
        # Auto-select template if only text is provided
        if use_ml and isinstance(texts, str) and not template_id:
            template_id = self.text_analyzer.suggest_template(texts, TEMPLATES)
            
        # Load template configuration
        template = TEMPLATES.get(template_id)
        if not template:
            raise ValueError(f"Unknown template: {template_id}")
            
        # Handle string input (split into top/bottom)
        if isinstance(texts, str):
            texts = [texts]
        
        # Load and prepare the template
        image = self.load_template(template_id)
        
        # Add text at each defined position
        for i, text in enumerate(texts):
            if text:
                if use_ml:
                    # Use ML to optimize position and size
                    position = self.text_analyzer.optimize_text_position(
                        text,
                        template.text_positions[i:i+1]  # Consider only valid positions for this text
                    )
                    size_ratio = self.text_analyzer.calculate_optimal_font_size(text, image.height)
                else:
                    position = template.text_positions[i]
                    size_ratio = template.default_font_size_ratio
                
                add_text_to_image(
                    image,
                    text.upper(),
                    position=(position.x_ratio, position.y_ratio),
                    max_width_ratio=position.max_width_ratio,
                    initial_size_ratio=size_ratio
                )
        
        if output_path:
            image.save(output_path, "JPEG", quality=JPEG_QUALITY)
        
        return image

from dataclasses import dataclass
from typing import List, Tuple, Optional

@dataclass
class TextPosition:
    x_ratio: float  # x position as ratio of image width (0.0 to 1.0)
    y_ratio: float  # y position as ratio of image height (0.0 to 1.0)
    max_width_ratio: float = 0.9  # maximum width as ratio of image width
    
@dataclass
class MemeTemplate:
    name: str
    filename: str
    text_positions: List[TextPosition]  # List of positions where text can be placed
    default_font_size_ratio: float = 0.1  # Font size as ratio of image height
    description: str = ""
    
# Define standard meme templates
TEMPLATES = {
    'drake': MemeTemplate(
        name='Drake',
        filename='drake.jpg',
        text_positions=[
            TextPosition(x_ratio=0.7, y_ratio=0.25),  # Top panel text
            TextPosition(x_ratio=0.7, y_ratio=0.75)   # Bottom panel text
        ],
        description="Drake Hotline Bling format - rejection vs. approval"
    ),
    'doge': MemeTemplate(
        name='Doge',
        filename='doge.jpg',
        text_positions=[
            TextPosition(x_ratio=0.5, y_ratio=0.2),  # Top text
            TextPosition(x_ratio=0.5, y_ratio=0.8)   # Bottom text
        ],
        description="Classic Doge meme with Comic Sans style text"
    ),
    'success': MemeTemplate(
        name='Success Kid',
        filename='success.jpg',
        text_positions=[
            TextPosition(x_ratio=0.5, y_ratio=0.15),  # Top text
            TextPosition(x_ratio=0.5, y_ratio=0.85)   # Bottom text
        ],
        description="Success Kid - celebrating achievements"
    ),
    'expanding_brain': MemeTemplate(
        name='Expanding Brain',
        filename='brain.jpg',
        text_positions=[
            TextPosition(x_ratio=0.75, y_ratio=0.15),  # First level
            TextPosition(x_ratio=0.75, y_ratio=0.38),  # Second level
            TextPosition(x_ratio=0.75, y_ratio=0.62),  # Third level
            TextPosition(x_ratio=0.75, y_ratio=0.85)   # Fourth level
        ],
        description="Expanding Brain - progression from basic to enlightened ideas"
    ),
    'disaster_girl': MemeTemplate(
        name='Disaster Girl',
        filename='disaster_girl.jpg',
        text_positions=[
            TextPosition(x_ratio=0.5, y_ratio=0.1),   # Top text
            TextPosition(x_ratio=0.5, y_ratio=0.9)    # Bottom text
        ],
        description="Disaster Girl - mischievous situations or chaotic outcomes"
    ),
    'distracted': MemeTemplate(
        name='Distracted Boyfriend',
        filename='distracted_boyfriend.jpg',
        text_positions=[
            TextPosition(x_ratio=0.25, y_ratio=0.15),  # Girl in front
            TextPosition(x_ratio=0.75, y_ratio=0.15),  # Girl behind
            TextPosition(x_ratio=0.5, y_ratio=0.85)    # Boyfriend
        ],
        default_font_size_ratio=0.08,  # Slightly smaller text due to three captions
        description="Distracted Boyfriend - comparing three things, usually with ironic preference"
    ),
    'hide_pain': MemeTemplate(
        name='Hide the Pain Harold',
        filename='hide_pain.jpg',
        text_positions=[
            TextPosition(x_ratio=0.5, y_ratio=0.15),  # Top text
            TextPosition(x_ratio=0.5, y_ratio=0.85)   # Bottom text
        ],
        description="Hide the Pain Harold - masking internal pain with a smile"
    ),
    'is_this': MemeTemplate(
        name='Is This a Pigeon',
        filename='is_this_pigeon.jpg',
        text_positions=[
            TextPosition(x_ratio=0.75, y_ratio=0.2),   # Top right (subject)
            TextPosition(x_ratio=0.5, y_ratio=0.85),   # Bottom (question)
            TextPosition(x_ratio=0.25, y_ratio=0.3)    # Left (person)
        ],
        default_font_size_ratio=0.08,  # Smaller text for better fit
        description="Is This a Pigeon - misidentifying or oversimplifying things"
    )
}

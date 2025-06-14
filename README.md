# Meme Generator with ML

An intelligent meme generator that uses machine learning to automatically select templates, position text, and optimize font sizes based on content.

## Features

- 🤖 AI-powered template selection
- 📏 Smart text positioning and sizing
- 🎨 Multiple popular meme templates supported
- 💪 Easy to use command-line interface
- 🎯 Optimized for readability and impact

## Supported Templates

- Drake (Hotline Bling format)
- Expanding Brain (4-panel progression)
- Distracted Boyfriend
- Is This a Pigeon?
- Hide the Pain Harold
- Disaster Girl
- Success Kid
- Doge

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/meme_generator.git
cd meme_generator
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Command Line Interface

1. Create a text file with your meme text:

For two-line memes (Drake, Success Kid, etc.):
```text
First line
Second line
```

For multi-line memes (Expanding Brain, Distracted Boyfriend):
```text
First line
Second line
Third line
Fourth line
```

2. Generate a meme:
```bash
# Basic usage
python generate_meme.py path/to/your/text.txt

# With custom output path
python generate_meme.py path/to/your/text.txt -o custom_output.jpg
```

### Python API

```python
from src.meme_generator import MemeGenerator

# Initialize the generator
generator = MemeGenerator()

# Auto-select template based on content
generator.create_meme(
    template_id=None,  # None for auto-selection
    texts="Your meme text here",
    output_path="meme.jpg"
)

# Use specific template
generator.create_meme(
    template_id="drake",
    texts=["First panel text", "Second panel text"],
    output_path="drake_meme.jpg"
)
```

## Examples

Check out the `examples/` directory for sample usage:
- `quick_start.py`: Basic usage examples
- `showcase_templates.py`: Examples with all templates
- `texts/`: Sample text files for different meme types

## Contributing

1. Fork the repository
2. Create your feature branch: `git checkout -b feature/amazing-feature`
3. Commit your changes: `git commit -m 'Add amazing feature'`
4. Push to the branch: `git push origin feature/amazing-feature`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- Thanks to all the meme creators who inspired these templates
- Built with PyTorch and Transformers for ML capabilities
- Uses NLTK for text analysis

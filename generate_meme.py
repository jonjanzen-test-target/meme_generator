import sys
import os
import argparse
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from src.meme_generator import MemeGenerator

def read_text_file(file_path):
    """Read text from file, supporting both single line and multi-line formats."""
    with open(file_path, 'r') as f:
        lines = [line.strip() for line in f.readlines() if line.strip()]
    
    # If there's only one line, return it as is
    if len(lines) == 1:
        return lines[0]
    # If there are multiple lines, return them as a list
    return lines

def generate_meme(text_file, output_path=None):
    """Generate a meme using the provided text."""
    # Initialize the generator
    generator = MemeGenerator()
    
    try:
        # Read the text from file
        text = read_text_file(text_file)
        
        # If output path is not provided, create one based on input filename
        if not output_path:
            base_name = os.path.splitext(os.path.basename(text_file))[0]
            output_path = f"{base_name}_meme.jpg"
            
        # Get list of available templates
        templates = generator.list_templates()
        if not templates:
            raise ValueError("No templates available!")
            
        # Let the text analyzer suggest a template
        text_analyzer = generator.text_analyzer
        suggested_template = text_analyzer.suggest_template(
            text if isinstance(text, str) else "\n".join(text),
            {tid: generator.get_template_info(tid) for tid in templates}
        )
        
        print(f"Selected template: {suggested_template}")
        
        # Generate the meme with the suggested template
        generator.create_meme(
            template_id=suggested_template,
            texts=text,
            output_path=output_path
        )
        print(f"\nMeme generated successfully! Saved as: {output_path}")
        
    except Exception as e:
        print(f"Error generating meme: {str(e)}")
        sys.exit(1)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Generate a meme from text in a file')
    parser.add_argument('text_file', help='Path to the text file containing meme text')
    parser.add_argument('-o', '--output', help='Output file path (optional)')
    
    # Parse arguments
    args = parser.parse_args()
    
    # Check if input file exists
    if not os.path.exists(args.text_file):
        print(f"Error: Text file '{args.text_file}' not found!")
        sys.exit(1)
    
    # Generate the meme
    generate_meme(args.text_file, args.output)

if __name__ == "__main__":
    main()

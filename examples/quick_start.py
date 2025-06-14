import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.meme_generator import MemeGenerator

def main():
    # Initialize the generator
    generator = MemeGenerator()
    
    # 1. Simple Drake meme
    print("Creating Drake meme...")
    generator.create_meme(
        template_id="drake",
        texts=[
            "Writing documentation",
            "Writing more code without documentation"
        ],
        output_path="drake_example.jpg"
    )
    
    # 2. Let AI choose the template
    print("\nLetting AI choose template...")
    generator.create_meme(
        template_id=None,
        texts="When the code works on the first try but you don't trust it",
        output_path="ai_choice.jpg"
    )
    
    # 3. Expanding Brain meme
    print("\nCreating Expanding Brain meme...")
    generator.create_meme(
        template_id="expanding_brain",
        texts=[
            "Using print statements",
            "Using debugger",
            "Using logging",
            "Adding random delays until it works"
        ],
        output_path="brain_example.jpg"
    )
    
    # 4. Distracted Boyfriend meme
    print("\nCreating Distracted Boyfriend meme...")
    generator.create_meme(
        template_id="distracted",
        texts=[
            "New Programming Language",
            "Your Current Stack",
            "You"
        ],
        output_path="distracted_example.jpg"
    )
    
    # 5. Is This a Pigeon meme
    print("\nCreating Is This a Pigeon meme...")
    generator.create_meme(
        template_id="is_this",
        texts=[
            "A minor bug",
            "Is this the end of the world?",
            "Project Manager"
        ],
        output_path="is_this_example.jpg"
    )
    
    print("\nAll memes generated! Check the output files in the current directory.")

if __name__ == "__main__":
    main()

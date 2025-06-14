from src.meme_generator import MemeGenerator

def main():
    # Initialize the meme generator
    generator = MemeGenerator()
    
    # List available templates
    print("Available templates:")
    for template_id in generator.list_templates():
        template = generator.get_template_info(template_id)
        print(f"- {template_id}: {template.description}")
    
    print("\nGenerating memes with ML optimization...")
    try:
        # Expanding Brain meme
        generator.create_meme(
            template_id="expanding_brain",
            texts=[
                "Using print statements",
                "Using a debugger",
                "Using logging",
                "Using telepathy with the CPU"
            ],
            output_path="brain_meme.jpg"
        )
        print("Expanding Brain meme generated!")
        
        # Distracted Boyfriend meme
        generator.create_meme(
            template_id="distracted",
            texts=[
                "New JavaScript Framework",
                "Existing Codebase",
                "Developers"
            ],
            output_path="distracted_meme.jpg"
        )
        print("Distracted Boyfriend meme generated!")
        
        # Is This a Pigeon meme
        generator.create_meme(
            template_id="is_this",
            texts=[
                "A bug",
                "Is this a feature?",
                "Product Manager"
            ],
            output_path="is_this_meme.jpg"
        )
        print("Is This a Pigeon meme generated!")
        
        # Hide the Pain Harold meme
        generator.create_meme(
            template_id="hide_pain",
            texts=[
                "When the client says they have a small change",
                "But it requires rewriting the entire codebase"
            ],
            output_path="hide_pain_meme.jpg"
        )
        print("Hide the Pain Harold meme generated!")
        
        # Disaster Girl meme
        generator.create_meme(
            template_id="disaster_girl",
            texts=[
                "Me watching my production server",
                "After running untested code"
            ],
            output_path="disaster_meme.jpg"
        )
        print("Disaster Girl meme generated!")
        
        # Test auto-template selection
        texts = [
            "When you accidentally push to production instead of staging",
            "Using AI to generate memes vs making them manually",
            "Is this what clean code looks like?",
            "When the code works but you don't know why"
        ]
        
        for i, text in enumerate(texts):
            generator.create_meme(
                template_id=None,  # Let ML choose the template
                texts=text,
                output_path=f"auto_meme_{i+1}.jpg"
            )
            print(f"Auto-template meme {i+1} generated!")
            
    except Exception as e:
        print(f"Error generating meme: {str(e)}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()

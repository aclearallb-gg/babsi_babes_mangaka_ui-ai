import random
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List

def create_character(characteristics: str) -> Dict[str, str]:
    """
    Create a character based on given characteristics.

    Args:
        characteristics (str): Comma-separated list of character traits.

    Returns:
        Dict[str, str]: A dictionary containing character information.
    """
    traits = characteristics.split(',')
    character = {
        'name': generate_name(),
        'traits': traits,
        'appearance': generate_appearance(),
        'backstory': generate_backstory(traits)
    }
    return character

def generate_name() -> str:
    """Generate a random Japanese name."""
    first_names = ['Akira', 'Yuki', 'Hana', 'Ryu', 'Mei']
    last_names = ['Tanaka', 'Sato', 'Watanabe', 'Yamamoto', 'Nakamura']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_appearance() -> str:
    """Generate a random appearance description."""
    hair_colors = ['black', 'brown', 'blonde', 'red', 'blue']
    eye_colors = ['brown', 'blue', 'green', 'gray', 'hazel']
    return f"Hair: {random.choice(hair_colors)}, Eyes: {random.choice(eye_colors)}"

def generate_backstory(traits: List[str]) -> str:
    """Generate a simple backstory based on character traits."""
    return f"A character with {', '.join(traits)} traits, seeking their place in the world."

def generate_character_card(character: Dict[str, str]) -> str:
    """
    Generate a character card image.

    Args:
        character (Dict[str, str]): Character information.

    Returns:
        str: Path to the generated character card image.
    """
    # Create a blank image
    img = Image.new('RGB', (300, 450), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 16)

    # Add character information to the card
    d.text((10,10), f"名前: {character['name']}", fill=(0,0,0), font=font)
    d.text((10,30), f"外見: {character['appearance']}", fill=(0,0,0), font=font)
    d.text((10,50), f"特性: {', '.join(character['traits'])}", fill=(0,0,0), font=font)
    d.text((10,70), f"背景: {character['backstory']}", fill=(0,0,0), font=font)

    # Save the image
    img_path = f"static/character_cards/{character['name'].replace(' ', '_')}.png"
    img.save(img_path)
    return img_path

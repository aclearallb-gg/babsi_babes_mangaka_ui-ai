import random
from PIL import Image, ImageDraw, ImageFont

def create_character(characteristics):
    traits = characteristics.split(',')
    character = {
        'name': generate_name(),
        'traits': traits,
        'appearance': generate_appearance(),
        'backstory': generate_backstory(traits)
    }
    return character

def generate_name():
    first_names = ['Akira', 'Yuki', 'Hana', 'Ryu', 'Mei']
    last_names = ['Tanaka', 'Sato', 'Watanabe', 'Yamamoto', 'Nakamura']
    return f"{random.choice(first_names)} {random.choice(last_names)}"

def generate_appearance():
    hair_colors = ['black', 'brown', 'blonde', 'red', 'blue']
    eye_colors = ['brown', 'blue', 'green', 'gray', 'hazel']
    return f"Hair: {random.choice(hair_colors)}, Eyes: {random.choice(eye_colors)}"

def generate_backstory(traits):
    return f"A character with {', '.join(traits)} traits, seeking their place in the world."

def generate_character_card(character):
    # Create a blank image
    img = Image.new('RGB', (300, 450), color = (255, 255, 255))
    d = ImageDraw.Draw(img)
    font = ImageFont.truetype("arial.ttf", 16)

    # Add character information to the card
    d.text((10,10), f"Name: {character['name']}", fill=(0,0,0), font=font)
    d.text((10,30), f"Appearance: {character['appearance']}", fill=(0,0,0), font=font)
    d.text((10,50), f"Traits: {', '.join(character['traits'])}", fill=(0,0,0), font=font)
    d.text((10,70), f"Backstory: {character['backstory']}", fill=(0,0,0), font=font)

    # Save the image
    img_path = f"static/character_cards/{character['name'].replace(' ', '_')}.png"
    img.save(img_path)
    return img_path

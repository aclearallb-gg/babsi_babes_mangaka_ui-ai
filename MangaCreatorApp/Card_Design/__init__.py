import random

def design_card(content):
    card = {
        'content': content,
        'style': generate_style(),
        'border': generate_border(),
        'font': generate_font()
    }
    return str(card)

def generate_style():
    styles = ['minimalist', 'ornate', 'futuristic', 'retro', 'hand-drawn']
    return random.choice(styles)

def generate_border():
    border_types = ['solid', 'dashed', 'dotted', 'double', 'none']
    colors = ['black', 'white', 'red', 'blue', 'gold']
    return f"{random.choice(border_types)} {random.choice(colors)}"

def generate_font():
    fonts = ['Arial', 'Helvetica', 'Times New Roman', 'Courier', 'Verdana']
    return random.choice(fonts)

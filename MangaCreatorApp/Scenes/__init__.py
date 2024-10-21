import random

def create_scene(description):
    scene_elements = description.split(',')
    scene = {
        'setting': generate_setting(scene_elements),
        'time_of_day': random.choice(['morning', 'afternoon', 'evening', 'night']),
        'weather': random.choice(['sunny', 'rainy', 'cloudy', 'stormy']),
        'mood': generate_mood(scene_elements)
    }
    return str(scene)

def generate_setting(elements):
    settings = ['city street', 'school', 'forest', 'beach', 'mountain']
    return random.choice(settings) if not elements else random.choice(elements)

def generate_mood(elements):
    moods = ['tense', 'peaceful', 'mysterious', 'romantic', 'adventurous']
    return random.choice(moods) if not elements else random.choice(elements)

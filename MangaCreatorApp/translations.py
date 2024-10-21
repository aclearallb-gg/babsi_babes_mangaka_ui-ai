translations = {
    'en': {
        'welcome': 'Welcome to the Manga Creator App',
        'story_generator': 'Story Generator',
        'character_creator': 'Character Creator',
        'scene_creator': 'Scene Creator',
        'card_designer': 'Card Designer',
        'project_management': 'Project Management',
        'language': 'Language',
        # Add more translations as needed
    },
    'ja': {
        'welcome': 'マンガクリエイターアプリへようこそ',
        'story_generator': 'ストーリージェネレーター',
        'character_creator': 'キャラクタークリエイター',
        'scene_creator': 'シーンクリエイター',
        'card_designer': 'カードデザイナー',
        'project_management': 'プロジェクト管理',
        'language': '言語',
        # Add more translations as needed
    }
}

def get_translation(key, lang='en'):
    return translations.get(lang, translations['en']).get(key, key)

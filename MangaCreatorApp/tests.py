import unittest
from main import app
from AI_Story_Generator import generate_story
from Character_Wizard import create_character
from Scenes import create_scene
from Card_Design import design_card

class MangaCreatorAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_generate_story(self):
        story = generate_story("Test prompt", ["Character1"], "Test scene")
        self.assertIsNotNone(story)

    def test_create_character(self):
        character = create_character("brave,strong")
        self.assertIn('name', character)
        self.assertIn('traits', character)

    def test_create_scene(self):
        scene = create_scene("forest,night")
        self.assertIsInstance(scene, str)

    def test_design_card(self):
        card = design_card("Test content")
        self.assertIsInstance(card, str)

if __name__ == '__main__':
    unittest.main()

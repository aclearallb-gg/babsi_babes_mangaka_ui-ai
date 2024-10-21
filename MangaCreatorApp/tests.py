import unittest
from main import app
from AI_Story_Generator import generate_story
from Character_Wizard import create_character, generate_character_card
from Scenes import create_scene
from Card_Design import design_card
from Storage_And_Undo import save_project, load_project, undo_action, auto_save

class MangaCreatorAppTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_home_page(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_generate_story(self):
        response = self.app.post('/generate_story', json={
            'prompt': 'Test prompt',
            'characters': ['Character1'],
            'scene': 'Test scene'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('story', response.json)

    def test_create_character(self):
        response = self.app.post('/create_character', json={
            'characteristics': 'brave,strong'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('character', response.json)

    def test_generate_character_card(self):
        character = create_character('brave,strong')
        response = self.app.post('/generate_character_card', json={
            'character': character
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('card', response.json)

    def test_create_scene(self):
        response = self.app.post('/create_scene', json={
            'description': 'forest,night'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('scene', response.json)

    def test_design_card(self):
        response = self.app.post('/design_card', json={
            'content': 'Test content'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('card', response.json)

    def test_save_and_load_project(self):
        project_data = {
            'story': 'Test story',
            'character': 'Test character',
            'scene': 'Test scene',
            'card': 'Test card'
        }
        save_response = self.app.post('/save_project', json={'project_data': project_data})
        self.assertEqual(save_response.status_code, 200)
        project_id = save_response.json['result'].split()[-1]
        
        load_response = self.app.get(f'/load_project?project_id={project_id}')
        self.assertEqual(load_response.status_code, 200)
        self.assertEqual(load_response.json['project_data'], project_data)

    def test_undo_action(self):
        response = self.app.post('/undo', json={'action_id': 'last'})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

    def test_auto_save(self):
        project_data = {
            'story': 'Auto-save test story',
            'character': 'Auto-save test character',
            'scene': 'Auto-save test scene',
            'card': 'Auto-save test card'
        }
        response = self.app.post('/auto-save', json={'project_data': project_data})
        self.assertEqual(response.status_code, 200)
        self.assertIn('result', response.json)

if __name__ == '__main__':
    unittest.main()

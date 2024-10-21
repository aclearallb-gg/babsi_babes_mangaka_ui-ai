from flask import Flask, render_template, request, jsonify, make_response
import logging
from werkzeug.exceptions import BadRequest, NotFound
from AI_Story_Generator import generate_story
from Character_Wizard import create_character, generate_character_card
from Scenes import create_scene
from Card_Design import design_card
from Storage_And_Undo import save_project, load_project, undo_action, auto_save
import os
from functools import wraps
from translations import get_translation

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'fallback_secret_key')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def handle_request(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError as e:
            logger.error(f"Missing key in request data: {e}")
            raise BadRequest(f"Missing key in request data: {e}")
        except Exception as e:
            logger.error(f"Error in {func.__name__}: {e}")
            return jsonify(error=f"An error occurred during {func.__name__}"), 500
    return wrapper

@app.errorhandler(BadRequest)
def handle_bad_request(e):
    logger.error(f"Bad request: {e}")
    return jsonify(error=str(e)), 400

@app.errorhandler(NotFound)
def handle_not_found(e):
    logger.error(f"Not found: {e}")
    return jsonify(error="Resource not found"), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
@handle_request
def story_generator():
    data = request.json
    story = generate_story(data['prompt'])
    return jsonify({'story': story})

@app.route('/create_character', methods=['POST'])
@handle_request
def character_creator():
    data = request.json
    character = create_character(data['characteristics'])
    return jsonify({'character': character})

@app.route('/generate_character_card', methods=['POST'])
@handle_request
def character_card_generator():
    data = request.json
    card = generate_character_card(data['character'])
    return jsonify({'card': card})

@app.route('/create_scene', methods=['POST'])
@handle_request
def scene_creator():
    data = request.json
    scene = create_scene(data['description'])
    return jsonify({'scene': scene})

@app.route('/design_card', methods=['POST'])
@handle_request
def card_designer():
    data = request.json
    card = design_card(data['content'])
    return jsonify({'card': card})

@app.route('/save_project', methods=['POST'])
@handle_request
def save_project_route():
    data = request.json
    result = save_project(data['project_data'])
    return jsonify({'result': result})

@app.route('/load_project', methods=['GET'])
@handle_request
def load_project_route():
    project_id = request.args.get('project_id')
    project_data = load_project(int(project_id))
    return jsonify({'project_data': project_data})

@app.route('/undo', methods=['POST'])
@handle_request
def undo_route():
    data = request.json
    result = undo_action(data['action_id'])
    return jsonify({'result': result})

@app.route('/language', methods=['POST'])
@handle_request
def set_language():
    data = request.json
    language = data['language']
    # Here you would typically set the language in the session or user preferences
    return jsonify({'result': f'Language set to {language}'})

@app.route('/scene-builder', methods=['GET', 'POST'])
@handle_request
def scene_builder():
    if request.method == 'POST':
        data = request.json
        scene = create_scene(data['elements'])
        return jsonify({'scene': scene})
    return render_template('scene_builder.html')

@app.route('/get_translation', methods=['POST'])
@handle_request
def get_translation_route():
    data = request.json
    translation = get_translation(data['key'], data.get('lang', 'en'))
    return jsonify({'text': translation})

@app.route('/auto-save', methods=['POST'])
@handle_request
def auto_save_route():
    data = request.json
    result = auto_save(data['project_data'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

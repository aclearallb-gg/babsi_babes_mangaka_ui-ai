from flask import Flask, render_template, request, jsonify
from AI_Story_Generator import generate_story
from Character_Wizard import create_character
from Scenes import create_scene
from Card_Design import design_card
from Storage_And_Undo import save_project, load_project, undo_action

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_story', methods=['POST'])
def story_generator():
    data = request.json
    story = generate_story(data['prompt'])
    return jsonify({'story': story})

@app.route('/create_character', methods=['POST'])
def character_creator():
    data = request.json
    character = create_character(data['characteristics'])
    return jsonify({'character': character})

@app.route('/create_scene', methods=['POST'])
def scene_creator():
    data = request.json
    scene = create_scene(data['description'])
    return jsonify({'scene': scene})

@app.route('/design_card', methods=['POST'])
def card_designer():
    data = request.json
    card = design_card(data['content'])
    return jsonify({'card': card})

@app.route('/save_project', methods=['POST'])
def save_project_route():
    data = request.json
    result = save_project(data['project_data'])
    return jsonify({'result': result})

@app.route('/load_project', methods=['GET'])
def load_project_route():
    project_id = request.args.get('project_id')
    project_data = load_project(project_id)
    return jsonify({'project_data': project_data})

@app.route('/undo', methods=['POST'])
def undo_route():
    data = request.json
    result = undo_action(data['action_id'])
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

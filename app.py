from flask import Flask, render_template, request, jsonify
from flask_apscheduler import APScheduler
app = Flask(__name__)
@app.route("/character-wizard", methods=["GET", "POST"])
def character_wizard(): return render_template("wizard.html")
@app.route("/scene-creator")
def scene_creator(): return render_template("scene_creator.html")
@app.route("/generate-story", methods=["POST"])
def generate_story(): data = request.json; response = {"story": "Sample story"}; return jsonify(response)
@app.route("/export", methods=["POST"])
def export(): return "Exporting..."

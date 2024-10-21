from flask import Flask, render_template, request, jsonify
      from flask_apscheduler import APScheduler
      from flask_babel import Babel

      app = Flask(__name__)
      app.config["SECRET_KEY"] = "your_secret_key"

      babel = Babel(app)
      scheduler = APScheduler()
      scheduler.init_app(app)
      scheduler.start()

      @babel.localeselector
      def get_locale():
          return request.accept_languages.best_match(["en", "de"])

      @app.route("/character-wizard", methods=["GET", "POST"])
      def character_wizard():
          return render_template("wizard.html")

      @app.route("/scene-creator")
      def scene_creator():
          return render_template("scene_creator.html")

      @app.route("/generate-story", methods=["POST"])
      def generate_story():
          data = request.json
          response = {"story": "Generated story based on: " + data["prompt"]}
          return jsonify(response)

      @app.route("/export", methods=["POST"])
      def export():
          return jsonify({"status": "Export successful"})

      if __name__ == "__main__":
          app.run(debug=True)

"""Widget service , a small Flask API used to demo the CircleCI pipeline."""
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.get("/widgets/count")
    def widget_count():
        # returns how many widgets are in stock
        widgets = ["sprocket", "gadget", "cog", "bolt"]
        return jsonify(count=len(widgets))

    return app

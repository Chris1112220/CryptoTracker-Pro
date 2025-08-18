
from flask import Flask


def create_app():
    app = Flask(__name__)

    @app.route("/health")
    def health():
        return {"status": "Up and running"}, 200

    return app

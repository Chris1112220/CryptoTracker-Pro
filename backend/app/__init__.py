
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///crypto.db"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    @app.route("/health")
    def health():
        return {"status": "Up and running"}, 200

    from app.routes import api
    app.register_blueprint(api, url_prefix="/api")

    return app

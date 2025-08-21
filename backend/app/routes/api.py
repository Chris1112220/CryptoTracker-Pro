from flask import Blueprint, jsonify

api = Blueprint("api", __name__)

@api.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to CryptoTracker-Pro API"})

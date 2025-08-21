from flask import Blueprint, request, jsonify
from app.models import db, User, Holding
from app.schemas import UserSchema, HoldingSchema

api = Blueprint("api", __name__)

# ---------------- USERS ---------------- #


@api.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()

    existing = User.query.filter_by(email=data["email"]).first()
    if existing:
        return jsonify({"error": "Email already registered"}), 400

    new_user = User(email=data["email"], password=data["password"])
    db.session.add(new_user)
    db.session.commit()

    return jsonify(UserSchema().dump(new_user)), 201  # ✅ FIXED


@api.route("/users", methods=["GET"])
def get_users():
    users = User.query.all()
    return jsonify(UserSchema(many=True).dump(users)), 200  # ✅ FIXED


# ---------------- HOLDINGS ---------------- #

@api.route("/holdings", methods=["POST"])
def create_holding():
    data = request.get_json()
    new_holding = Holding(
        user_id=data["user_id"],
        coin=data["coin"],
        amount=data["amount"],
        cost_basis=data["cost_basis"]
    )
    db.session.add(new_holding)
    db.session.commit()

    return jsonify(HoldingSchema().dump(new_holding)), 201  # ✅ FIXED


@api.route("/holdings", methods=["GET"])
def get_holdings():
    holdings = Holding.query.all()
    return jsonify(HoldingSchema(many=True).dump(holdings)), 200  # ✅ FIXED

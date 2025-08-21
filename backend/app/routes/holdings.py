from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import db
from app.models import Holding
from app.schemas import HoldingSchema

holdings_bp = Blueprint("holdings", __name__)


@holdings_bp.get("/")
@jwt_required()
def get_holdings():
    user_id = get_jwt_identity()
    holdings = Holding.query.filter_by(user_id=user_id).all()
    return jsonify(HoldingSchema(many=True).dump(holdings))


@holdings_bp.post("/")
@jwt_required()
def create_holding():
    user_id = get_jwt_identity()
    data = request.get_json()

    if not data.get("coin") or not data.get("amount"):
        return jsonify({"error": "coin and amount are required"}), 400

    holding = Holding(
        user_id=user_id,
        coin=data["coin"],
        amount=float(data["amount"]),
        cost_basis=float(data.get("cost_basis", 0))
    )
    db.session.add(holding)
    db.session.commit()

    return jsonify(HoldingSchema().dump(holding)), 201

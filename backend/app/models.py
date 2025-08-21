from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    holdings = db.relationship("Holding", backref="user", lazy=True)


class Holding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    coin = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    cost_basis = db.Column(db.Float, nullable=True)

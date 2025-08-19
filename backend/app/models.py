from . import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)


class Holding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    coin = db.Column(db.String(50), nullable=False)
    amount = db.Column(db.Float, nullable=False)
    cost_basis = db.Column(db.Float, nullable=False)

    user = db.relationship("User", backref="holdings")

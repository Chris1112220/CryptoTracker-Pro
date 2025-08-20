from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
from app.models import User, Holding


class HoldingSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Holding
        load_instance = True


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True
        include_relationships = True  # ✅ boolean, not function call

    holdings = HoldingSchema(many=True)  # ✅ put it here, not inside Meta

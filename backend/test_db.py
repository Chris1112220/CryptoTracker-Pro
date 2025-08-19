from app import create_app, db
from app.models import User, Holding

app = create_app()

with app.app_context():
    # Create a test user
    user = User(email="test2@example.com", password="hashedpassword123")
    db.session.add(user)
    db.session.commit()

    # Create a holding for that user
    holding = Holding(
        user_id=user.id,
        coin="Bitcoin",
        amount=0.5,
        cost_basis=20000
    )
    db.session.add(holding)
    db.session.commit()

    print("✅ Test user and holding inserted!")

    # Query back user and holdings
    user = User.query.first()
    print("User:", user.email)

    for h in user.holdings:
        print(
            f"Holding: {h.coin}, {h.amount} units, Cost Basis: ${h.cost_basis}")

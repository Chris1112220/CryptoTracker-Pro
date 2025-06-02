from app import create_app  # ✅ this will now work because 'app' is inside 'backend'

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

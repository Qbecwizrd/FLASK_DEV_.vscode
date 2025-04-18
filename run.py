from app import create_app # type: ignore

# Set the database URI here
database_uri = "sqlite:///data.db"

# Create the Flask app
app = create_app(database_uri)

# Run the Flask development server
if __name__ == "__main__":
    app.run(debug=True)  # Set debug=True for development, remove it for production

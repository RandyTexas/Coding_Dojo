from flask_app import app
from flask_app.controllers import login_pages

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)


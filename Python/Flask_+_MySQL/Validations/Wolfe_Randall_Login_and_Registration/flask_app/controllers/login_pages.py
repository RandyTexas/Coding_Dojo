from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_bcrypt import Bcrypt
from flask_app.models.login_page import User
bcrypt = Bcrypt(app) 

# Login and Registration page routes
@app.route("/")
def index():
    session.clear()
    return redirect("/login")

@app.route("/login")
def login():
    return render_template("login_page.html")

# When Clicked on the login button, the form data is sent to the server and the server will check if the user exists in the database. 
# If the user exists, the server will check if the password matches the hashed password in the database. 
# If the password matches, the user will be redirected to the dashboard. 
# If the password does not match, the user will be redirected to the login page with a flash message. 
# If the user does not exist, the user will be redirected to the login page with a flash message.
@app.route("/register", methods=['POST'])
def register():
    User.validate_user_login(request.form)
    if not User.validate_user_login(request.form):
        flash("Invalid registration information", "error")
        return redirect('/login')
    User.create_user(request.form)
    return redirect('/dashboard')



# Take you to the dashboard (index.html) page
@app.route("/dashboard")
def dashboard():
    return render_template('index.html')

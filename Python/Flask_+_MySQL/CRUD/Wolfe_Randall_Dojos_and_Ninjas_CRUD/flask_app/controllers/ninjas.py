# from flask_app.models.ninja import Ninja
# from flask_app.models.dojo import Dojo
from flask import render_template,redirect,request,session
from flask_app import app



@app.route("/ninja")
def ninja():
    return render_template("ninja.html")
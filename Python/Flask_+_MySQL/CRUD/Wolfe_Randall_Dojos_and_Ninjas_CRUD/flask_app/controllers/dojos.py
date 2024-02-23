from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route("/")
def home():
    session.clear()
    return redirect("/dojo")

@app.route("/dojo")
def dojo():
    dojos = Dojo.get_all()
    return render_template("dojo.html", dojos = dojos)
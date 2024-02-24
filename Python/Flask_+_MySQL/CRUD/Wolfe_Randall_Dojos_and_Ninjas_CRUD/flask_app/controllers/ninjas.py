from flask import render_template,redirect,request
from flask_app import app
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo



@app.route("/ninja")
def ninja():
    return render_template("ninja.html", dojos = Dojo.get_all())

@app.route("/ninja_create", methods = ["POST"])
def ninja_create():
    Ninja.save(request.form)
    return redirect("/")
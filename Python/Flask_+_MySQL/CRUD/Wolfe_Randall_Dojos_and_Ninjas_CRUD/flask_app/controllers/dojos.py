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



@app.route("/dojo_create", methods = ["POST"])
def dojos():
    Dojo.save(request.form)
    return redirect("/dojo")


@app.route("/dojo/<int:id>")
def dojo_show(id):
    data = {
        "id": id
    }
    dojo = Dojo.get_one(data)
    return render_template("dojo_show.html", dojo = dojo)
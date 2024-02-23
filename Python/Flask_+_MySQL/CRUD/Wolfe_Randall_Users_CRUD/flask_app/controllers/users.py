from flask import render_template,redirect,request,session
from flask_app import app
from flask_app.models.user import Users



# Create
@app.route("/")
def index():
    session.clear()
    return redirect("/create")

@app.route("/create")
def create():
    return render_template("create.html")

@app.route("/create", methods=["POST"])
def add_user():
    Users.save_users(request.form)
    return redirect("/read")



# Read
@app.route("/read")
def veiw_all_users():
    all_users = Users.get_all()
    return render_template("view_all.html", users = all_users)
    
    
@app.route("/read/<int:user_id>")
def read(user_id):
    one_user = Users.get_one(user_id)
    return render_template("view_user.html", user = one_user)



# Update
@app.route("/update/<int:user_id>")
def update_id(user_id):
    one_user = Users.get_one(user_id)
    return render_template("edit_user.html", user = one_user)

@app.route("/update", methods=["POST"])
def update_user():
    Users.update(request.form)
    return redirect("/read")


# Delete
@app.route('/delete/<int:user_id>')
def delete(user_id):
    Users.delete(user_id)
    return redirect('/read')



# @app.route("/delete/<int:id>")
# def delete(id):
#     data = {
#         "id": id
#     }
#     Users.delete(data)
#     return redirect("/")

# @app.route("/delete/<int:id>", methods=["POST"])
# def delete_user(id):
#     data = {
#         "id": id
#     }
#     Users.delete(data)
#     return redirect("/")



from flask import render_template,redirect,session,request
from flask_app import app 
from flask_app.models.user import Users



@app.route('/')
def index():
    # session.clear()
    return render_template("Create.html")

















    

# @app.route('/create', methods=['GET', 'POST'])
# def user_info():   
#     if 'user' not in session:
#         if request.method == 'GET':
#             return render_template("Create.html")
        
#     else: 
#         if request.method == 'POST':
#             form = request.form
#             users = session['user']
#             users.append({
#                 "id": len(users)+1,
#                 "first_name": form['first_name'],
#                 "last_name": form['last_name'],
#                 "email": form['email']
#             })
#             session['user'] = Users.save_users(form)
#             print(users)
            
#             return redirect('/read')
#     session['user'] = []
#     form = request.form
#     users = session['user']
    
#     users.append({
#         "id": len(users)+1,
#         "first_name": form['first_name'],
#         "last_name": form['last_name'],
#         "email": form['email']
#     })
#     session['user'] = Users.save_users(form)
#     print(users)
    
#     return redirect('/read')

# @app.route('/read', methods=['GET'])
# def users_info():
#     if 'user' not in session:
#         return redirect('/')
#     else:
#         return render_template("Read.html", user=Users.get_all())





from flask import Flask, render_template, redirect, request
from user import User


app = Flask(__name__)
app.secret_key='secret'

@app.route('/')
def index():
    return render_template('home.html', users = User.get_all())


@app.route('/add_user')
def add_user():
    return render_template('add.html')


@app.route('/create', methods=['POST'])
def new_user():
    User.save(request.form)
    print(request.form)
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)





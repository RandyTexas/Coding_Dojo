from flask import Flask, render_template, redirect, session

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    return redirect('/counter')

@app.route('/counter')
def counter():
    if 'counter' in session:
        session['counter'] += 1
    else:
        session['counter'] = 1
    return render_template('index.html', counter=session['counter'])

@app.route('/destroy_session')
def destroy_session():
    session.clear()
    return redirect('/counter')

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)



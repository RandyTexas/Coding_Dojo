from flask import Flask, render_template, redirect, request, session
import random

app = Flask(__name__)
app.secret_key = 'SecretKey'

@app.route('/')
def index():
    return redirect('/game')

@app.route('/game')
def game():
    if 'number' not in session:
        session['number'] = random.randint(1, 100)
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    guess = int(request.form['guess'])
    number = session['number']
    message = ""
    if guess < number:
        message = "Too low! Try again."
    elif guess > number:
        message = "Too high! Try again."
    else:
        message = f"Congratulations! You've guessed the number {number}!"
        session.pop('number')
    return render_template('index.html', message=message)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)

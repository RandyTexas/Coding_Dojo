from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "Secret"

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/survey', methods=['POST'])
def survey_info():
    session['name'] = request.form['name']
    session['locations'] = request.form['locations']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return render_template('survey.html', session=session)

if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=8000)



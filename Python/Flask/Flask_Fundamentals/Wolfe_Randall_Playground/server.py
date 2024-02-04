from flask import Flask, render_template # Import Flask to allow us to create our app

app = Flask(__name__)    

@app.route('/')
def main():
    return "Put a /play at the end of the URL link!"

# Level 1

@app.route('/play')         
def play():
    return render_template("index.html", num = 3, color = "blue")

#level 2

@app.route('/play/<int:x>')
def x(x):
    return render_template("index.html", num = x, color = "blue")

# Level 3
@app.route('/play/<int:x>/<string:color>')
def colors(x,color):
    return render_template("index.html", num = x, color = color)


if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)
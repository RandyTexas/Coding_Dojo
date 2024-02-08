from flask import Flask, render_template
app = Flask(__name__)
# our index route will handle rendering our form
@app.route('/')
def index():
    return render_template("index.html")

def hello_world():
    return 'Hello World!'  
if __name__=="__main__":     
    app.run(debug=True, host="localhost", port=8000) 


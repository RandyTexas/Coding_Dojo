from flask import Flask, render_template

app = Flask(__name__)    

# http://localhost:8000 - should display 8 by 8 checkerboard
@app.route('/')
def main():
    return render_template('index.html', x=4, y=4, color1="black", color2="grey")

# http://localhost:8000/4 - should display 8 by 4 checkerboard
@app.route('/<int:rows>')
def rows(rows):
    return render_template('index.html', x=rows, y=4, color1="black", color2="grey")

# http://localhost:8000/x/y - should display x by y checkerboard
@app.route('/<int:rows>/<int:cols>')
def rows_cols(rows, cols):
    return render_template('index.html', x=rows, y=cols, color1="black", color2="grey")

# http://localhost:8000/x/y/color1 - should display x by y checkerboard with color1
@app.route('/<int:rows>/<int:cols>/<string:color1>')
def color1(rows, cols, color1):
    return render_template('index.html', x=rows, y=cols, color1= color1, color2= "grey")

# http://localhost:8000/x/y/color1/color2 - should display x by y checkerboard with color1 and color2
@app.route('/<int:rows>/<int:cols>/<string:color1>/<string:color2>')
def color2(rows, cols, color1, color2):
    return render_template('index.html', x=rows, y=cols, color1= color1, color2= color2)



if __name__=="__main__":
    app.run(debug=True, host="localhost", port=8000)
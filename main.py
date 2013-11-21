from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/detail")
def detail():
    return render_template('detail.html')

@app.route("/apply")
def apply():
    return render_template('apply.html')

if __name__=="__main__":
    app.run(debug=True)

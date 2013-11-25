from flask import Flask, render_template, url_for
app = Flask(__name__)
app.debug=True
app.host="0.0.0.0"

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/detail")
def detail():
    return render_template('detail.html')

@app.route("/apply")
def apply():
    return render_template('apply.html')

@app.route("/test/<int:username>")
def test(username):
    return url_for("apply")

if __name__=="__main__":
    app.run()

from flask import Flask, render_template, request, flash 

app = Flask(__name__)
app.secret_key = "stringsuponchars_123456789"

@app.route("/contact")

def index():
    flash("For collaboration, songwriting and production, or to say hello, share name & email")
    return render_template("index.html")

@app.route("/hello", methods=["POST", "GET"])
def hello():
    flash("Hey " + str(request.form['name_input']) + ", I'll be in touch soon!")
    return render_template("index.html")
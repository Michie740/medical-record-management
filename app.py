from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        return "<p>Logged in!</p>"

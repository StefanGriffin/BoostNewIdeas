from flask import render_template, request
from src import app


@app.route("/data/")
def data():
    return render_template("data.html")

@app.route("/greet/", methods=["GET", "POST"])
def greet():
    if request.method == "GET":
        return render_template("data_html")
    if request.method == "POST":
        return render_template("greet.html", name=request.form.get("name"))





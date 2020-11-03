from flask import render_template, request
from src import app


@app.route("/data/")
def data():
    return render_template('data.html')

@app.route("/greet/")
def greet():
    return render_template('greet.html', name=request.args.get('name'))





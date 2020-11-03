from flask import render_template
from src import app


@app.route("/data/")
def data():
    return render_template('data.html')
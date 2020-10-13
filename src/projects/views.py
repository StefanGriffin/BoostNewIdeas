from flask import render_template
from src import app


@app.route("/projects/")
def projects():
    return render_template('projects.html')
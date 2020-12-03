from flask import render_template
from src import app


@app.route("/social media/")
def socialmedia():
    return render_template('socialmedia.html')
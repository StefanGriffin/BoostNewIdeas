from flask import render_template, request
from src import app

PROJECTS = [
    "Numpy",    
    "Pandas",
    "Matplotlib",
]


REGISTRANTS = {

}


@app.route("/data/")
def data():
    return render_template("data.html", projects=PROJECTS)

@app.route("/register/", methods=["POST"])
def register():
    name = request.form.get("name")
    if not name:
        return render_template("error.html", message = "Missing name")
    project = request.form.get("project")
    if not project:
        return render_template("error.html", message = "Missing project")
    if project not in PROJECTS:
        return render_template("error.html", message = "Invalid project")

    REGISTRANTS[name] = project
    print(REGISTRANTS)

    return render_template("success.html")

    







        






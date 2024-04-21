from flask import render_template, Blueprint 

routes = Blueprint("routes",__name__)

@routes.route('/home')
def home():
    return render_template("base.html")

@routes.route("/login")
def login():
    return render_template("login.html")
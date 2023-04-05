from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    title = "Home"
    css_route = "css/home.css"
    return render_template("home.html", title=title, css_route=css_route)
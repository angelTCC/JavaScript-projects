from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route("/")
def index():
    return render_template("index.html")

@main.route("/reviewcarousel")
def about():
    return render_template("reviewcarousel.html")


@main.route("/scrolling")
def scrolling():
    return render_template("scrolling.html")


@main.route("/userfilter")
def UserFilter():
    return render_template("UserFilter.html")

@main.route("/tabsection")
def TabSection():
    return render_template("TabSection.html")

@main.route("/todolist")
def ToDoList():
    return render_template("todolist.html")

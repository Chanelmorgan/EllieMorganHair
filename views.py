from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/") 
def home(): 
    return render_template("index.html")


@views.route("/contact")
def contact(): 
    return render_template("contact.html")

@views.route("/go-to-home")
def go_to_home(): 
    return redirect(url_for("views.home"))
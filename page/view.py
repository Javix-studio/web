from flask import Blueprint,render_template,redirect,url_for

view= Blueprint( __name__ ,"view")

@view.route("/")
def home():
    return render_template("index.html")

@view.route("/Home")
def HOME():
    return redirect(url_for("view.home"))

@view.route("/About")
def about():
    return render_template("about.html")

@view.route("/Contact")
def contact():
    return render_template("contact.html")

@view.route("/Links")
def links():
    return render_template("links.html")


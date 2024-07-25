# -*- coding: utf-8 -*-
import argparse
from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm
# url_for is a function that will find exact route that we are looking for


app = Flask(__name__)
app.config["SECRET_KEY"] = "gjhfgoiljkft679676tyhfvnmm "


my_posts = [
    {
        "title": "My first (1) blog post",
        "author": "Usman Musa",
        "pub_date": "May 25, 2020",
        "summary": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odit totam dolore ipsa ipsum facilis. Aliquid at doloribus qui ipsam enim exercitationem similique, quidem adipisci nesciunt nostrum consectetur nobis pariatur aperiam!"
    },
    
    {
        "title": "My second (2) blog post",
        "author": "Usman Musa",
        "pub_date": "May 25, 2020",
        "summary": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odit totam dolore ipsa ipsum facilis. Aliquid at doloribus qui ipsam enim exercitationem similique, quidem adipisci nesciunt nostrum consectetur nobis pariatur aperiam!"
    },
    
    {
        "title": "My third (3) blog post",
        "author": "Usman Musa",
        "pub_date": "May 25, 2020",
        "summary": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Odit totam dolore ipsa ipsum facilis. Aliquid at doloribus qui ipsam enim exercitationem similique, quidem adipisci nesciunt nostrum consectetur nobis pariatur aperiam!"
    }
]


@app.route("/")
def home():
    return render_template("home.html", title="home page", posts=my_posts)


@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}!", "success")
        return redirect(url_for("home"))
    return render_template("register.html", title="Register", form=form)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == "admin@blog.com" and form.password.data == "password":
            flash("You have been logged in!", "success")
            return redirect(url_for("home"))
        else:
            flash("Login Unsuccessful. Please check username and password", "danger")
    return render_template("login.html", title="Login", form=form)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--port", "-p", type=int, default=5000)
    parser.add_argument("--host", "-H", default="127.0.0.1")
    parser.add_argument("--debug", "-d", default=False, type=bool)
    args = parser.parse_args()
    app.run(debug=args.debug, port=args.port, host=args.host)

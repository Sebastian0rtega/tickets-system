from flask import Blueprint, render_template, request, redirect, session
from models.user_model import *
from base_datos import *


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        user = get_user_by_credentials(email, password)

        if not user:
            return render_template("login.html", error="Credenciales incorrectas")

        session["user_id"] = user["id"]
        session["role"] = user["role"]

        if user["role"] == "USER":
            return redirect("/usuario")
        else:
            return redirect("/tecnico")

    return render_template("login.html")

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        create_user(email, password)

        return redirect("/")

    return render_template("register.html")


@auth_bp.route("/logout")
def logout():
    session.clear()
    return redirect("/")

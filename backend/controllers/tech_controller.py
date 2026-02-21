from flask import Blueprint, render_template, session, redirect, request
from models.ticket_model import *
from models.user_model import create_user_with_role


tech_bp = Blueprint("tech", __name__)



@tech_bp.route("/tecnico")
def tecnico():

    if "user_id" not in session or session["role"] != "TECH":
        return redirect("/")

    estado = request.args.get("estado")

    if estado:
        tickets = get_tickets_by_status(estado)
    else:
        tickets = get_all_tickets()

    return render_template("tecnico.html", tickets=tickets)



@tech_bp.route("/tickets/estado", methods=["POST"])
def cambiar_estado():

    update_ticket_status(
        request.form["ticket_id"],
        request.form["status"]
    )

    return redirect("/tecnico")


@tech_bp.route("/crear_usuario", methods=["GET", "POST"])
def crear_usuario():

    if "role" not in session or session["role"] != "TECH":
        return redirect("/")

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]
        role = request.form["role"]

        create_user_with_role(email, password, role)

        return redirect("/tecnico")

    return render_template("crear_usuario.html")
from flask import Blueprint, render_template, session, redirect
from models.ticket_model import get_tickets_by_user

user_bp = Blueprint("user", __name__)

@user_bp.route("/usuario")
def usuario():
    if "user_id" not in session or session["role"] != "USER":
        return redirect("/")

    tickets = get_tickets_by_user(session["user_id"])
    return render_template("usuario.html", tickets=tickets)

from flask import Blueprint, render_template, session, redirect, request
from models.ticket_model import get_all_tickets, update_ticket_status

tech_bp = Blueprint("tech", __name__)

@tech_bp.route("/tecnico")
def tecnico():
    if "user_id" not in session or session["role"] != "TECH":
        return redirect("/")
    tickets = get_all_tickets()
    return render_template("tecnico.html", tickets=tickets)

@tech_bp.route("/tickets/estado", methods=["POST"])
def cambiar_estado():
    update_ticket_status(
        request.form["ticket_id"],
        request.form["status"]
    )
    return redirect("/tecnico")


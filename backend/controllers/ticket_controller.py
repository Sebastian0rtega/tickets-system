from flask import Blueprint, render_template, request, redirect, session
from models.ticket_model import crear_ticket_db

ticket_bp = Blueprint("ticket", __name__)

@ticket_bp.route("/tickets/crear", methods=["GET", "POST"])
def crear_ticket():
    if "user_id" not in session:
        return redirect("/")

    if request.method == "POST":
        titulo = request.form["title"]
        descripcion = request.form["descripcion"]
        categoria = request.form["categoria"]

        crear_ticket_db(
            titulo,
            descripcion,
            categoria,
            session["user_id"]
        )
    
        return redirect("/usuario")
    return render_template("crear_ticket.html")


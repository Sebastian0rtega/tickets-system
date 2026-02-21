from db import get_db

def crear_comentario(ticket_id, user_id, content):

    db = get_db()

    db.execute("""
    INSERT INTO comments (ticket_id, user_id, content)
    VALUES (?, ?, ?)
    """, (ticket_id, user_id, content))

    db.commit()


def obtener_comentarios(ticket_id):

    db = get_db()

    return db.execute("""
    SELECT c.content, u.email
    FROM comments c
    JOIN users u ON u.id = c.user_id
    WHERE ticket_id = ?
    """, (ticket_id,)).fetchall()

def asignar_ticket(ticket_id, tech_id):

    db = get_db()

    db.execute("""

    UPDATE tickets

    SET technician_id = ?

    WHERE id = ?

    """, (tech_id, ticket_id))

    db.commit()
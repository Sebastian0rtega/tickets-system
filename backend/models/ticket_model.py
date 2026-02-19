from db import get_db
from datetime import datetime


def crear_ticket_db(title, description, category, user_id):

    db = get_db()
    cur = db.cursor()

    cur.execute("""
        INSERT INTO tickets
        (title, description, category, status, user_id)
        VALUES (?, ?, ?, 'ABIERTO', ?)
    """,
    (
        title,
        description,
        category,
        user_id
    ))


def get_tickets_by_user(user_id):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT id, title, description, category, status
        FROM tickets
        WHERE user_id = ?
        ORDER BY id DESC
    """, (user_id,))
    return cur.fetchall()

def get_all_tickets():
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        SELECT t.id, t.title, t.description, t.category, t.status,
               u.email
        FROM tickets t
        JOIN users u ON u.id = t.user_id
        ORDER BY t.id DESC
    """)
    return cur.fetchall()

def update_ticket_status(ticket_id, status):
    db = get_db()
    cur = db.cursor()
    cur.execute("""
        UPDATE tickets SET status = ?
        WHERE id = ?
    """, (status, ticket_id))
    db.commit()
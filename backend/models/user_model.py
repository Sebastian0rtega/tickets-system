from db import get_db

def get_user_by_credentials(email, password):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT id, role FROM users WHERE email=? AND password=?",
        (email, password)
    )
    return cur.fetchone()

def create_user(email, password):

    db = get_db()
    cursor = db.cursor()

    cursor.execute("""
        INSERT INTO users (email, password, role)
        VALUES (?, ?, 'USER')
    """, (email, password))

    db.commit()

def create_user_with_role(email, password, role):

    db = get_db()

    db.execute("""
        INSERT INTO users (email, password, role)
        VALUES (?, ?, ?)
    """, (email, password, role))

    db.commit()
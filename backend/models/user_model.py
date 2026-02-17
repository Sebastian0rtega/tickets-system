from db import get_db

def get_user_by_credentials(email, password):
    db = get_db()
    cur = db.cursor()
    cur.execute(
        "SELECT id, role FROM users WHERE email=? AND password=?",
        (email, password)
    )
    return cur.fetchone()

import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def get_db():
    db_path = os.path.join(BASE_DIR, "base_datos", "tickets.db")
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row   
    return conn
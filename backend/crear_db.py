import sqlite3
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

db_path = os.path.join(BASE_DIR, "base_datos", "tickets.db")

os.makedirs(os.path.join(BASE_DIR, "base_datos"), exist_ok=True)

conn = sqlite3.connect(db_path)

cursor = conn.cursor()

cursor.executescript("""

CREATE TABLE users (

id INTEGER PRIMARY KEY AUTOINCREMENT,

email TEXT UNIQUE,

password TEXT,

role TEXT

);


CREATE TABLE tickets (

id INTEGER PRIMARY KEY AUTOINCREMENT,

title TEXT,

description TEXT,

category TEXT,

importance TEXT,

status TEXT,

created_at TEXT,

user_id INTEGER,

technician_id INTEGER

);


CREATE TABLE comments (

id INTEGER PRIMARY KEY AUTOINCREMENT,

ticket_id INTEGER,

user_id INTEGER,

content TEXT,

created_at TEXT

);

""")


cursor.execute(

"INSERT INTO users VALUES (NULL,'user@test.com','123','USER')"

)

cursor.execute(

"INSERT INTO users VALUES (NULL,'tech@test.com','123','TECH')"

)

conn.commit()

conn.close()

print("BASE DE DATOS CREADA EN:", db_path)
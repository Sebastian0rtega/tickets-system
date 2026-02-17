import sqlite3

conn = sqlite3.connect("base_datos/tickets.db")
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
  status TEXT,
  user_id INTEGER,
  technician_id INTEGER
);

CREATE TABLE comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  ticket_id INTEGER,
  user_id INTEGER,
  content TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
""")

cursor.execute("INSERT INTO users VALUES (NULL,'user@test.com','123','USER')")
cursor.execute("INSERT INTO users VALUES (NULL,'tech@test.com','123','TECH')")
conn.commit()
conn.close()
print("Base de datos creada")
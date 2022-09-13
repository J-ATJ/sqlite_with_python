import sqlite3

conn = sqlite3.connect("soccer.sqlite")
cur = conn.cursor()

cur.execute(
    "INSERT INTO player (name, nationality, age) VALUES (?, ?, ?)",
    ("Ronaldo", "Portugal", 37),
)
cur.execute(
    "INSERT INTO player (name, nationality, age) VALUES (?, ?, ?)",
    ("Messi", "Argentina", 35),
)
cur.execute(
    "INSERT INTO player (name, nationality, age) VALUES (?, ?, ?)",
    ("Neymar", "Brazil", 30),
)
conn.commit()

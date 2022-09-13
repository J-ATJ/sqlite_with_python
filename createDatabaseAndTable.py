import sqlite3

conn = sqlite3.connect("soccer.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS player")
cur.execute("CREATE TABLE player (name TEXT, nationality TEXT, age INTEGER)")

conn.close()

import sqlite3

conn = sqlite3.connect("soccer.sqlite")
cur = conn.cursor()

cur.execute("DROP TABLE IF EXISTS player")
conn.commit()

cur.close()

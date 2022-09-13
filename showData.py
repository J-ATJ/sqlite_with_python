import sqlite3

conn = sqlite3.connect("soccer.sqlite")
cur = conn.cursor()

print("Table player")
cur.execute("SELECT * FROM player")
for row in cur:
    print(row)

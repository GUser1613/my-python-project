import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute("UPDATE students SET age=? WHERE id=?", (25, 1))

conn.commit()
conn.close()

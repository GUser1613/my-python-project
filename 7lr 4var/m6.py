import sqlite3

conn = sqlite3.connect("students.db")
cur = conn.cursor()

cur.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    ("Владимир", 23)
)

conn.commit()
conn.close()
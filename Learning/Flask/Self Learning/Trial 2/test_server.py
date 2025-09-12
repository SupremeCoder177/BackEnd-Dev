import sqlite3 as sql

conn = sql.connect("dummy.db")
cur = conn.cursor()

print("Running script....")
try:
    res = cur.execute("SELECT * FROM BLOGS")
    data = res.fetchall()
    for row in data:
        print(row)
except sql.ProgrammingError:
    print("Error occured !")
finally:
    conn.close()
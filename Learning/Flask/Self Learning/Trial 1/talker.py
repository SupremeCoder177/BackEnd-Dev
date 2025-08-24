# a simple script to talk with and modify the database file in the current directory

import sqlite3 as sql
import os

os.chdir(os.path.split(os.path.abspath(__file__))[0])

con = sql.connect('dummy.db')
cur = con.cursor()

print("Talking with database, enter 'exit' to exit and commit changes, or enter -1 to exit whtout committing changes")
while True:
    command = str(input(">"))

    if command.lower() == "exit":
        con.commit()
        con.close()
        break
    
    if command == "-1":
        con.close()
        break

    try:
        res = cur.execute(command)
        print("Here is the database response:")
        for ch in res.fetchall():
            print(ch)
    except Exception as e:
        print("An en error has occured.")

from flask import Flask, render_template, url_for, request
import sqlite3 as sql
from typing import List

app = Flask(__name__)

"""
BLOGS TABLE CONTENT
(i) BLOG_ID
(ii) USERNAME
(iii) IMAGEPATH
(iv) EMAIL
(v) CONTENT
(vi) LIKES
"""
"""
USERS TABLE
(i) USER_ID
(ii) USERNAME
(iii) EMAIL
(iv) PASSWORD
"""


def run_and_commit_command(command):
    conn = sql.connect('dummy.db')
    cur = conn.cursor()
    res = cur.execute(command)
    conn.commit()
    data = None
    try:
        data = res.fetchall()
    except sql.ProgrammingError:
        pass
    conn.close()
    return data


def create_table(name : str, params : List[str]):
    conn = sql.connect("dummy.db")
    cur = conn.cursor()

    temp = " ,".join(params)
    command = f'CREATE TABLE {name} ({temp})'

    try:
        cur.execute(command)
    except sql.DatabaseError:
        print("Something went wrong while table creation")
    finally:
        conn.commit()
        conn.close()



@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html", blogs=run_and_commit_command("SELECT * FROM BLOGS"))

@app.route("/post", methods=["GET"])
def post_blog():
    return render_template('post.html')

@app.route("/sign-up", methods=["GET"])
def sign_up():
    return render_template('sign_up.html')

@app.route("/login", methods=["GET"])
def login_page():
    return render_template('login.html')

@app.route("/login-user", methods=["POST"])
def login():
    data = request.get_json()
    print(data)
    for arg in request.args:
        print(arg)

    return {"success" : False, "message" : "user did not login successfully"}

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
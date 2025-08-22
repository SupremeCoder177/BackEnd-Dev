from flask import Flask, render_template, jsonify, url_for
import sqlite3 as s
import os

app = Flask(__name__)
os.chdir("F:\\Backend\\Learning\\Flask\\Self Learning\\Trial 1")

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    db_con = s.connect("dummy.db")
    db_cur = db_con.cursor()
    res = db_cur.execute("SELECT * from POSTS")
    return render_template("index.html", posts=res.fetchall())

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html")

@app.route("/post", methods=["GET"])
def add_post():
    return render_template('add_post.html')
    

if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)
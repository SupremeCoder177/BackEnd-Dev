from flask import Flask, render_template, url_for
import sqlite3 as sql

app = Flask(__name__)

# BLOGS TABLE CONTENT
# (i) USERNAME
# (ii) IMAGEPATH
# (iii) EMAIL
# (iv) CONTENT
# (v) CREATED
# (vi) LIKES
# (vii) COMMENTS


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
    

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/post", methods=["GET"])
def post_blog():
    return render_template('post.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
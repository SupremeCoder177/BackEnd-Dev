from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/", methods=["GET"])
@app.route("/home", methods=["GET"])
def home():
    return render_template("index.html")

@app.route("/post", methods=["GET"])
def post_blog():
    return render_template('post.html')

if __name__ == "__main__":
    app.run(host="localhost", port=5000)
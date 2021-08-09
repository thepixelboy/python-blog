import requests
from flask import Flask, render_template

app = Flask(__name__)
blog_posts = requests.get("https://api.npoint.io/e42b353ee387383898c7").json()


@app.route("/")
def home():
    return render_template("index.html", posts=blog_posts)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


if __name__ == "__main__":
    app.run(debug=True)

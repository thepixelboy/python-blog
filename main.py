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


@app.route("/post/<int:post_id>")
def post(post_id):
    for post in blog_posts:
        if post["id"] == post_id:
            title = post["title"]
            subtitle = post["subtitle"]
            image = post["image"]
            date = post["date"]
            author = post["author"]
            body = post["body"]
    return render_template(
        "post.html", title=title, subtitle=subtitle, image=image, date=date, author=author, body=body
    )


if __name__ == "__main__":
    app.run(debug=True)

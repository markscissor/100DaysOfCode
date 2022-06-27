from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)
data = None


def get_data():
    global data
    blog_url = "https://api.npoint.io/34bce8386c620589b1c4"
    r = requests.get(blog_url)
    data = Post(r.json()['blog'])


@app.route('/')
def home():
    global data
    if data is None:
        get_data()
    return render_template("index.html", posts=data.posts)

@app.route('/post/<int:blog_id>')
def show_post(blog_id):
    global data
    if data is None:
        get_data()
    blog = data.get_post(blog_id)
    return render_template("post.html", post=blog)

if __name__ == "__main__":
    app.run(debug=True)

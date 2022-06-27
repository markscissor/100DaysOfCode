from flask import Flask, render_template
app = Flask(__name__)
from random import randint
from datetime import datetime
import requests


@app.route('/')
def serve():
    return render_template('index.html', num = randint(0, 9), current_year = datetime.now().year)

@app.route('/guess/<name>')
def guess(name):
    age_url = f"https://api.agify.io?name={name.lower()}"
    gender_url = f"https://api.genderize.io?name={name.lower()}"

    agify = requests.get(age_url)
    age = agify.json()['age']

    genderize = requests.get(gender_url)
    gender = genderize.json()['gender']

    return render_template('result.html', age=age, gender=gender, name=name.title(), current_year = datetime.now().year)

@app.route('/blog/<num>')
def get_blog(num):
    blog_url = "https://api.npoint.io/34bce8386c620589b1c4"
    r = requests.get(blog_url)
    all_posts = r.json()['blog']

    return render_template('blog.html', posts=all_posts)



if __name__ == '__main__':
    app.run(debug=True)

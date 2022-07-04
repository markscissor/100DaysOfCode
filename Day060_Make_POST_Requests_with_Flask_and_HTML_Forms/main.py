from flask import Flask, render_template, request
import requests
from datetime import datetime
from notification import NotificationManager


notification_manager = NotificationManager()

app = Flask(__name__)

data = None

def get_data():
    global data
    if data is None:
        blog_url = "https://api.npoint.io/d824ed4f6601ae09f535"
        r = requests.get(blog_url)
        data = r.json()
        for datum in data:
            datum['date'] = datetime.strptime(datum['date'], "%Y-%m-%d").strftime("%B %-d, %Y")



@app.route('/')
def home():
    global data
    get_data()
    return render_template('index.html', posts=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:blog_id>')
def post(blog_id):
    global data
    get_data()
    blog = data[blog_id - 1]
    return render_template("post.html", post=blog)

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/form-entry', methods=['POST'])
def receive_data():
    name = request.form['name']
    email = request.form['email']
    phone = request.form['phone']
    message = request.form['message']

    SUBJECT = "Contact Form Submission"
    MESSAGE = f"name: {name}\nemail: {email}\nphone: {phone}\nmessage: {message}"
    notification_manager.send_emails(
        ['corroro_001@yahoo.com'],
        SUBJECT,
        MESSAGE
    )

    return render_template('contact.html')


if __name__ == '__main__':
    app.run(debug=True)
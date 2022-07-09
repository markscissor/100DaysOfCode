from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory, flash, abort
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField
from wtforms.validators import DataRequired
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

app = Flask(__name__)
bootstrap = Bootstrap(app)

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))
#Line below only required once, when creating DB. 
# db.create_all()

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Let me in.", validators=[DataRequired()])

class RegisterForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()], render_kw={"placeholder": "Name"})
    email = StringField("Email", validators=[DataRequired()], render_kw={"placeholder": "Email"})
    password = PasswordField("Password", validators=[DataRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField("Sign me up.", validators=[DataRequired()])



@app.route('/')
def home():
    return render_template("index.html")


@app.route('/register', methods=[ 'GET', 'POST'])
def register():
    form = RegisterForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            if User.query.filter_by(email=form.email.data).first():
                #User already exists
                flash("You've already signed up with that email, log in instead!")
                return redirect(url_for('login'))
            new_user = User(
                email = request.form.get('email'),
                password = generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8),
                name = request.form.get('name')
            )
            db.session.add(new_user)
            db.session.commit()

            #Log in and authenticate user after adding details to database.
            login_user(new_user)

            return redirect( url_for('secrets'))
            
    return render_template("register.html", form=form)


@app.route('/login', methods=[ 'GET', 'POST'])
def login():
    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            # Login and validate the user.
            # user should be an instance of your `User` class
            user = User.query.filter_by(email=form.email.data).first()
            # User not found
            if not user:
                flash("That email does not exist, please try again.")
                return redirect(url_for('login'))
            # Wrong password
            elif not check_password_hash(user.password, form.password.data):
                flash('Password incorrect, please try again.')
                form.password.data = ''
                return render_template("login.html", form=form, email=True)
            else:
                login_user(user)
                flash('Logged in successfully.')
                return redirect( url_for('secrets'))

    return render_template("login.html", form=form)


@app.route('/secrets')
@login_required
def secrets():
    print(current_user.name)
    return render_template("secrets.html")


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route('/download')
@login_required
def download():
    return send_from_directory('static/files/', 'cheat_sheet.pdf')


if __name__ == "__main__":
    app.run(debug=True)

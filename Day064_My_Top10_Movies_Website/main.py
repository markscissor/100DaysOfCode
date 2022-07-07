from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os
from dotenv import load_dotenv


load_dotenv()


MOVIEDB_API = 'https://api.themoviedb.org/3'
IMAGE_URL_ENDPOINT = 'https://image.tmdb.org/t/p/w500'
MOVIEDB_KEY = os.environ['MOVIEDB_KEY']

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/my-top-10-movies.db'.format(os.getcwd())
db = SQLAlchemy(app)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.FLOAT(80), nullable=True)
    ranking = db.Column(db.Integer, nullable=True)
    review = db.Column(db.String(255), nullable=True)
    img_url = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<Movie %r>' % self.title

db.create_all()

# new_movie = Movie(
#     title="Phone Booth",
#     year=2002,
#     description="Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",
#     rating=7.3,
#     ranking=10,
#     review="My favourite character was the caller.",
#     img_url="https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg"
# )
# db.session.add(new_movie)
# db.session.commit()


class ReviewForm(FlaskForm):
    rating = StringField('Your Rating Ouf of 10 e.g. 7.5', validators=[DataRequired()])
    review = StringField('Your Review', validators=[DataRequired()])
    submit = SubmitField('Done')

class MovieForm(FlaskForm):
    title = StringField('Movie Title', validators=[DataRequired()])
    submit = SubmitField('Add Movie')

@app.route("/")
def home():
    movies = db.session.query(Movie).order_by(Movie.rating)
    movie_count = movies.count()
    for idx, movie in enumerate(movies):
        movie.ranking = movie_count - idx

    return render_template("index.html", movies=movies)

@app.route('/edit/<int:movie_id>', methods=['GET', 'POST'])
def edit(movie_id):
    form = ReviewForm()
    movie_to_update = Movie.query.get(movie_id)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_rating = form.rating.data
            movie_to_update.rating = new_rating
            new_review = form.review.data
            movie_to_update.review = new_review
            db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', form=form,  movie=movie_to_update)

@app.route('/delete/<int:movie_id>')
def delete(movie_id):
    movie_to_delete = Movie.query.get(movie_id)
    db.session.delete(movie_to_delete)
    db.session.commit()
    return redirect(url_for('home'))

@app.route("/add", methods=['GET', 'POST'])
def add():
    form = MovieForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            params = {
                'api_key': MOVIEDB_KEY,
                'query': form.title.data
            }
            endpoint = f"{MOVIEDB_API}/search/movie"
            response = requests.get(url=endpoint, params=params)
            data = response.json()['results']
        return render_template("select.html", data=data)
    else:
        return render_template("add.html", form=form)

@app.route('/select/<int:movie_id>')
def select(movie_id):
    params = {
        'api_key': MOVIEDB_KEY
    }
    endpoint = f"{MOVIEDB_API}/movie/{movie_id}"
    response = requests.get(url=endpoint, params=params)
    data = response.json()

    new_movie = Movie(
        title = data['title'],
        year = data['release_date'].split('-')[0],
        description = data['overview'],
        img_url = f"{IMAGE_URL_ENDPOINT}{data['backdrop_path']}"
    )
    db.session.add(new_movie)
    db.session.flush()
    db.session.commit()

    return redirect(url_for('edit',  movie_id=new_movie.id))

if __name__ == '__main__':
    app.run()

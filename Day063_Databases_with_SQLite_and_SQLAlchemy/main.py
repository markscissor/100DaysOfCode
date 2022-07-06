from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///{}/new-books-collection.db'.format(os.getcwd())
db = SQLAlchemy(app)

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    author = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.FLOAT(80), nullable=False)

    def __repr__(self):
        return '<Book %r>' % self.title

db.create_all()
# book1 = Book(title='Harry Potter', author='J.K. Rowling', rating=9.3)
# db.session.add(book1)
# db.session.commit()





@app.route('/')
def home():
    all_books = db.session.query(Book).all()
    print(all_books)
    return render_template('index.html', books=all_books)


@app.route("/add", methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        book_name = request.form.get('book_name')
        book_author = request.form.get('book_author')
        rating = request.form.get('rating')
        book1 = Book(title=book_name, author=book_author, rating=rating)
        db.session.add(book1)
        db.session.commit()

        return redirect(url_for('home'))
    else:
        return render_template('add.html')

@app.route('/edit/<int:book_id>', methods=['GET', 'POST'])
def edit(book_id):
    book_to_update = Book.query.get(book_id)
    if request.method == 'POST':
        new_rating = request.form.get('rating')
        book_to_update.rating = new_rating
        db.session.commit()
        return redirect(url_for('home'))
    else:
        return render_template('edit.html', book=book_to_update)

@app.route('/delete/<int:book_id>')
def delete(book_id):
    book_to_delete = Book.query.get(book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))



if __name__ == "__main__":
    app.run()


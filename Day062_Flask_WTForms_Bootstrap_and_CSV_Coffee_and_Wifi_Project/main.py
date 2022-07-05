from flask import Flask, render_template, url_for, request, redirect
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField, TimeField
from wtforms.validators import DataRequired
from flask_datepicker import datepicker
from datetime import datetime as dt
import csv

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField('Cafe Location on Google Maps (URL)', validators=[DataRequired()])
    opening = TimeField('Opening Time', validators=[DataRequired()], default=dt.strptime("08:00", "%H:%M"))
    closing = TimeField('Closing Time', validators=[DataRequired()], default=dt.strptime("17:30", "%H:%M"))
    coffee_rating = SelectField('Coffee Rating', choices=['☕','☕☕','☕☕☕','☕☕☕☕','☕☕☕☕☕'], validators=[DataRequired()])
    wifi_rating = SelectField('Wifi Strength Rating', choices=['💪','💪💪','💪💪💪','💪💪💪💪','💪💪💪💪💪'], validators=[DataRequired()])
    power_socket = SelectField('Power Socket Availability', choices=['🔌','🔌🔌','🔌🔌🔌','🔌🔌🔌🔌','🔌🔌🔌🔌🔌'], validators=[DataRequired()])
    submit = SubmitField('Submit')

# Exercise:
# add: Location URL, open time, closing time, coffee rating, wifi rating, power outlet rating fields
# make coffee/wifi/power a select element with choice of 0 to 5.
#e.g. You could use emojis ☕️/💪/✘/🔌
# make all fields required except submit
# use a validator to check that the URL field has a URL entered.
# ---------------------------------------------------------------------------


# all Flask routes below
@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['GET', 'POST'])
def add_cafe():
    form = CafeForm()
    if request.method == 'GET':
        return render_template('add.html', form=form)

    elif request.method == 'POST':
        if form.validate_on_submit():
            print("True")
            with open('cafe-data.csv', 'a', newline='') as csv_file:
                open_str = form.opening.data.strftime("%-I:%M%p")
                close_str = form.closing.data.strftime("%-I:%M%p")
                form_data = f"{form.cafe.data},{form.location.data},{open_str},{close_str},{form.coffee_rating.data},{form.wifi_rating.data},{form.power_socket.data}\n"
                print(form_data)
                csv_file.write(form_data)
        return redirect(url_for('cafes'))
    # Exercise:
    # Make the form write a new row into cafe-data.csv
    # with   if form.validate_on_submit()
    


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
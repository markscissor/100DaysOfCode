from flask import Flask, jsonify, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import random
import re

app = Flask(__name__)

##Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def rand_cafe():
    cafes = Cafe.query.all()
    r_cafe = random.choice(cafes)
    response = jsonify(
        id = r_cafe.id,
        name = r_cafe.name,
        map_url = r_cafe.map_url,
        img_url = r_cafe.img_url,
        location = r_cafe.location,
        seats = r_cafe.seats,
        has_toilet = r_cafe.has_toilet,
        has_wifi = r_cafe.has_wifi,
        has_sockets = r_cafe.has_sockets,
        can_take_calls = r_cafe.can_take_calls,
        coffee_price = r_cafe.coffee_price
    )
    return response
    

## HTTP GET - Read Record
@app.route("/all")
def get_cafes():
    cafes = Cafe.query.all()
    cafe_list = []
    for cafe in cafes:
        cafe_list.append({
            "id": cafe.id,
            "name": cafe.name,
            "map_url": cafe.map_url,
            "img_url": cafe.img_url,
            "location": cafe.location,
            "seats": cafe.seats,
            "has_toilet": cafe.has_toilet,
            "has_wifi": cafe.has_wifi,
            "has_sockets": cafe.has_sockets,
            "can_take_calls": cafe.can_take_calls,
            "coffee_price": cafe.coffee_price
        })
    response = jsonify(cafe_list)
    return response

@app.route('/search')
def search():
    loc = request.args.get('loc')
    cafes = Cafe.query.all()
    local_cafes = []
    for cafe in cafes:
        result = re.search(loc, cafe.location, re.IGNORECASE)
        if result is not None:
            local_cafes.append({
                "id": cafe.id,
                "name": cafe.name,
                "map_url": cafe.map_url,
                "img_url": cafe.img_url,
                "location": cafe.location,
                "seats": cafe.seats,
                "has_toilet": cafe.has_toilet,
                "has_wifi": cafe.has_wifi,
                "has_sockets": cafe.has_sockets,
                "can_take_calls": cafe.can_take_calls,
                "coffee_price": cafe.coffee_price
            })

    if not len(local_cafes):
        return jsonify({
            "error": {
                "Not Found": "Sorry, we don't have a cafe at that location."
            }
        })
    else:
        return jsonify(local_cafes)

## HTTP POST - Create Record
@app.route("/add", methods=["POST"])
def add():
    try:
        if not request.args.get('api_key') == 'TopSecretAPIKey':
            return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
        new_cafe = Cafe(
            name = request.form['name'],
            map_url = request.form['map_url'],
            img_url = request.form['img_url'],
            location = request.form['location'],
            seats = request.form['seats'],
            has_toilet = bool(request.form['has_toilet']),
            has_wifi = bool(request.form['has_wifi']),
            has_sockets = bool(request.form['has_sockets']),
            can_take_calls = bool(request.form['can_take_calls']),
            coffee_price = request.form['coffee_price']
        )
        db.session.add(new_cafe)
        db.session.commit()
        return jsonify({
            "response": {
                "success": "Successfully added the new cafe."
            }
        })

    except (ValueError, TypeError) as e:
        pass


    return jsonify({
        "response": {
            "faillure": "Failed to add the new cafe."
        }
    })

## HTTP PUT/PATCH - Update Record
@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    try:
        cafe_to_update = Cafe.query.get(cafe_id)

        ### Update all atributes
        # for k, v in request.form.items():
        #     if not v == "":
        #         print(k)
        #         if k in ['has_toilet', 'has_wifi', 'has_sockets', 'can_take_calls']:
        #             if v == 'false' or v == 'False':
        #                 setattr(cafe_to_update, k, False)
        #             else:
        #                 setattr(cafe_to_update, k, True)
        #         else:
        #             setattr(cafe_to_update, k, v)

        # Update the price
        cafe_to_update.coffee_price = request.args.get('new_price')
        db.session.commit()
        
        
        return jsonify({
            "success": "Successfully updated the price."
        }), 200
    except (ValueError, TypeError, AttributeError) as e:
        pass

    return jsonify({
        "error": {
            "Not Found": "Sorry the cafe with that id was not found in the database."
        }
    }), 404


## HTTP DELETE - Delete Record
@app.route('/report-closed/<cafe_id>', methods=['DELETE'])
def delete(cafe_id):
    try:
        if not request.args.get('api_key') == 'TopSecretAPIKey':
            return jsonify({"error": "Sorry, that's not allowed. Make sure you have the correct api_key."}), 403
        cafe_to_delete = Cafe.query.get(cafe_id)
        if cafe_to_delete:
            db.session.delete(cafe_to_delete)
            db.session.commit()
        
            return jsonify({
                "success": "Successfully deleted the cafe."
            }), 200
    except (ValueError, TypeError, AttributeError) as e:
        pass

    return jsonify({
        "error": {
            "Not Found": "Sorry the cafe with that id was not found in the database."
        }
    }), 404

if __name__ == '__main__':
    app.run(debug=True)

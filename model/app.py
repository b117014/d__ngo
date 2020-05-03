import os
import csv;
from model import *
from flask import render_template,request,Flask

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://prabhatku:1234@localhost/airport"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)   # Tie up Database with flask application

def main():
    db.create_all()    # create database
    file = open('./data/flights.csv')
    data = csv.reader(file)
    for origin,destination,duration in data:
        flight = Flights(origin=origin,destination=destination,duration=duration)
        db.session.add(flight)
    db.session.commit()

    


if __name__ == "__main__":
    with app.app_context():
        main()


# SELECT * FROM fligts    ===    Fligts.query.all()
#  SELECT * FROM flights WHERE origin = "Paris"    ===   Flights.query.filter_by(origin="Paris").all()

# SELECT COUNT(*) from flights where origin = "Paris"    === Flights.query.filter_by(origin="Paris").count()

# SELECT * FROM flights WHERE id = 28         ===   Flights.query.get(28) || Flights.query.filter_by(id=28).first()
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Flights(db.Model):        # db.model means flihts class inherits the db class
    __tablename__ = 'flights'     # to define the table name
    id = db.Column(db.Integer,primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    passangers = db.relationship("Passangers",backref="flight",lazy=True)    # extract all passengers in this flight

    def add_passanger(self,name):
        p = Passangers(name=name,flight_id=self.id)
        db.session.add(p)
        db.session.commit()

class Passangers(db.Model):
    __tablename__ = 'passangers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey('flights.id'),nullable=False)     # adding foreign key


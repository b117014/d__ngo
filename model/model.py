from flask_sqlalchemy import SQLAlchemy;

db = SQLAlchemy()

class Fligts(db.model):        # db.model means flihts class inherits the db class
    __tablename__ = 'fligts'
    id = db.Column(db.Integer,primary_key=True)
    origin = db.Column(db.String, nullable=False)
    destination = db.Column(db.String, nullable=False)
    duration = db.Column(db.Integer, nullable=False)

class Passangers(db.model):
    __tablename__ = 'passangers'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String,nullable=False)
    flight_id = db.Column(db.Integer,db.ForeignKey('fligts.id'),nullable=False)     # adding foreign key
    

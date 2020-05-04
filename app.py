from flask import Flask,render_template,request,session
from flask_session import Session
import datetime
from model.model import *
app = Flask(__name__)    # __name__ represent the current file

# for server side render
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)


app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://prabhatku:1234@localhost/airport"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

@app.route("/")          # after the default routes open the browser just below function is called
def index():
    flights = Flights.query.filter_by(origin="Patna").all()
    print(flights[0].destination)
    return render_template('index.html',data=flights)

@app.route("/hello")
def hello():
    return "hello"

@app.route("/name/<string:name>")      # <string:name> denotes the name is variable that can put on the route and use in function
def name_(name):
    return render_template('first.html',name=name)

@app.route('/newyear')
def newYear():
    date = datetime.datetime.now();
    new_year = date.day == 1 and date.month==1
    return render_template('first.html',new_year=new_year,date=date)

@app.route('/home',methods=["POST"])              # post route in flask
def home():
    session['notes'] = []
    name = request.form.get('home')            # request.form.get() method to request the input data and works similar to req.body
    session['notes'].append(name)
    print(name)
    return render_template('index.html',name=name)

@app.route('/add',methods=["POST"])
def add():
    flight_id = request.form.get('flight_id')
    flight = Flights.query.get(flight_id)
    name = request.form.get('name')
    flight.add_passanger(name)

@app.route('/passanger/<int:id>')
def passanger(id):
    flight = Flights.query.get(id)
    passenger = flight.passangers;
    print(passenger)
    return "hello"


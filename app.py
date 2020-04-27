from flask import Flask,render_template,request,session
from flask_session import Session
import datetime

app = Flask(__name__)    # __name__ represent the current file

# for server side render
app.config["SESSION_PERMANENT"] = False
app.config['SESSION_TYPE'] = 'filesystem'
Session(app)

@app.route("/")          # after the default routes open the browser just below function is called
def index():
    return "Hi there"

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


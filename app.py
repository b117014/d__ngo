from flask import Flask,render_template

app = Flask(__name__)    # __name__ represent the current file

@app.route("/")          # after the default routes open the browser just below function is called
def index():
    return "Hi there"

@app.route("/hello")
def hello():
    return "hello"

@app.route("/name/<string:name>")      # <string:name> denotes the name is variable that can put on the route and use in function
def name_(name):
    return render_template('first.html')
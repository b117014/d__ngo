from flask import Flask

app = Flask(__name__)    # __name__ represent the current file

@app.route("/")          # after the default routes open the browser just below function is called
def index():
    return "Hi there"
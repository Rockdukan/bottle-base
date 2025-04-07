from bottle import template

from app import app


@app.route("/")
def index():
    return template("index", name="Bottle")

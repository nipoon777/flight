from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.exceptions import default_exceptions
from cs50 import SQL


app = Flask(__name__)

db = SQL("postgres://iwcuuvojalcppu:300be0bc205b34207dbbd18218b8155c0fa69730eeb0497ef1bca3670a34b834@ec2-54-235-86-101.compute-1.amazonaws.com:5432/d2d3alomvpcnov")

@app.route("/")
def index():
    flights = db.execute("SELECT * FROM flights")
    return render_template("index.html",flights = flights)

@app.route("/book",methods=["POST"])
def book():

    name = request.form.get("name")
    try:
        flight_id = int(request.form.get("flight_id"))
    except ValueError:
        return render_template("error.html", message="Invalid flight number.")

    return render_template("success.html")

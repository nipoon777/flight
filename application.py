from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.exceptions import default_exceptions
from cs50 import SQL

app = Flask(__name__)

db = SQL("sqlite:///flight.db")

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

    db.execute("INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)",
            name = name, flight_id =flight_id )

    return render_template("success.html")

from app import app
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request


courses = [("Real Estate Finance", 73528), ("Moral Theology", 49264),
           ("Software Engineering", 25484), ("Social Media Mgt", 47205),
           ("EIRP Honors", 64284)]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html", courses = courses)

@app.route("/add_course")
def add_course():
    return render_template("index.html")


@app.route("/register_student", methods = ['GET, 'POST'])
def register_student():
    return render_template(" ")

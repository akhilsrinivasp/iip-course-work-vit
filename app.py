from cmd import IDENTCHARS
from email.message import EmailMessage
from enum import unique
from re import template

from flask import Flask, render_template
from flask import request
from flask import url_for

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder = 'templates')
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.sqlite3"
app.config['SECRET_KEY'] = 'ThisisSecretKey'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class user(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, autoincrement = True, primary_key=True)
    name = db.Column(db.String, nullable = False)
    email = db.Column(db.String, nullable = False,  primary_key=True, unique = True)
    pan = db.Column(db.String, nullable = False,  primary_key=True, unique =True)
    password = db.Column(db.String, nullable = False)

class transactions(db.Model):
    __tablename__ = 'transactions'
    sender = db.Column(db.Integer, db.ForeignKey("user.ID"), primary_key = True, nullable = False)
    receiver = db.Column(db.Integer, db.ForeignKey("user.ID"), primary_key = True, nullable = False)
    amount = db.Column(db.Integer, nullable = False)
    type = db.Column(db.String, db.CheckConstraint("Type = 'NEFT' OR Type = 'RTGS'"))    

class RegisterForm(FlaskForm):
    user_name = StringField

@app.route('/', methods=["GET", "POST"])
def hello_world():
    welcome_text = 'Welcome to the netbanking portal'
    return render_template("index.html", display_name = welcome_text)

@app.route("/login", methods=["GET", "POST"])
def login(): 
    if request.method == "GET":
        return render_template('/login_page/login.html')
    if request.method == "POST":
        users = user.query.all()
        return render_template('/dashboard/dash.html', users = users)
    
@app.route("/forgot_password")
def forgot():
    return render_template("/login_page/forgot.html")
    

@app.route("/register")
def register_new():
    
    return render_template("/login_page/register.html")

if __name__ == '__main__':
    app.run(
        debug=True,
        host='0.0.0.0',
        port=8080
    )
    
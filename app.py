from flask import Flask, render_template
from flask import request
from flask import url_for
app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def hello_world():
    name = "Akhil"
    return render_template("index.html", display_name=name)


@app.route("/login", methods=["GET", "POST"])
def login(): 
    return render_template('/login_page/login.html')

@app.route("/forgot_password")
def forgot():
    return render_template("/login_page/forgot.html")
    
@app.route("/register")
def register_new():
    return render_template("/login_page/register.html")

if __name__ == '__main__':
    app.debug=True
    app.run()
    
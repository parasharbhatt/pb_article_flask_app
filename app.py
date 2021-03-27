

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/home", methods=["GET","POST"])
def home():
    return render_template("home.html")
    


#print("hello world")

from flask import Flask         # from the flask module, import the Flask class
from flask import render_template

# OOP - Object Oriented Paradigm 
app = Flask(__name__)           # Initialize the Flask class into app, now an object.


@app.get("/")                   # Flask decorator that creates routes
def index():
    me = {                      # Python dictionary (key and value pairs)
        "first_name": "Adam",
        "last_name": "Young",
        "hobbies": "basketball",
        "is_active": True
    }
    return me                   # With Flask, returning a valid dictionary from a 
                                # view function will automatically cover it to 
                                # JSON
@app.get("/about")
def about_me():
    return render_template("about.html")

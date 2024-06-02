from flask import Flask,jsonify,json
from flask_cors import CORS
app=Flask(__name__)
CORS(app)
@app.route('/')
def inital():
    return 'Hello World'
@app.route('/data')
def first():
    dat={
        "name":"Shadman Sakib Mahee",
        "ID":19201103123,
        "Dept":"CSE",
    }
    return jsonify(dat)
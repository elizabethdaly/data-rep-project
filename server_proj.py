# Server for the project

#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

# List of foods (or a DB)
# Price is a float .xx
foods=[
    {"id": 1, "name":"cheese", "price": 2.50},
    {"id": 2, "name":"carrots", "price:": 1.10},
    {"id": 3, "name":"milk", "price:": 1.97}
]

# Keep track of ID as need to increment for new food
# This is a global var
nextId = 3

# Maybe have a shopping basket later?
basket=[
    {"id": 1, "name":"chedder", "amount": 2},
    {"id": 2, "name":"carrots", "amount:": 0},
    {"id": 3, "name":"milk", "amount:": 1}
]
# Keep track of ID as need to increment for new food in basket
basketId = 4

# Action = Get all
# curl "http://127.0.0.1:5000/foods"
@app.route('/foods')
def getAll():
    #return "in getAll"

    return jsonify(foods)

if __name__ == '__main__' :
    app.run(debug= True)
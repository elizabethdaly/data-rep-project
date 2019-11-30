# Server for the project

#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

##################################################################
# List of foods (or a DB)
# Price is a float .xx
foods=[
    {"id": 1, "category": "Dairy", "name":"cheese", "price": 2.50},
    {"id": 2, "category": "Vegetable","name":"carrots", "price:": 1.10},
    {"id": 3, "category": "Dairy","name":"milk", "price:": 1.97}
]

# Keep track of ID as need to increment for new food
# This is a global var
nextId = 4

##################################################################
# Maybe have another array for second DB like a cart?
cart=[
    {"id": 1, "name":"chedder", "amount": 2},
    {"id": 2, "name":"carrots", "amount:": 0},
    {"id": 3, "name":"milk", "amount:": 1}
]
# Keep track of ID as need to increment for new food in basket
cartId = 4
##################################################################

# Action = Get all
# curl "http://127.0.0.1:5000/foods"
@app.route('/foods')
def getAll():
    #return "in getAll"

    return jsonify(foods)

##################################################################

# Action = Find food by ID
# curl "http://127.0.0.1:5000/foods/1"
@app.route('/foods/<int:id>')
def findByID(id):
    #return "in find by ID for id "+ str(id)

    #for each f in foods, check id until match
    foundFoods = list(filter(lambda f: f['id'] == id, foods))
    
    # Maybe print error message?
    if len(foundFoods) == 0:
        return jsonify({}), 204

    # Else return the food by requested id
    return jsonify(foundFoods[0])

##################################################################

# Action = Create a new food
# curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"steak\", \"category\":\"Meat\", \"price\": 2.50 }" "http://127.0.0.1:5000/foods"
@app.route('/foods', methods=['POST'])
def create():
    global nextId # To allow edits inside this function
    #return "in create"

    if not request.json:
        abort(400)

    # Do other checking for more marks eg proper format?
    # price must be a float

    # id increments automatically
    # Suppy name and price in request
    food = {
        "id": nextId,
        "category": request.json['category'],
        "name": request.json['name'],
        "price": request.json['price']
    }

    nextId += 1
    foods.append(food)
    return jsonify(food)

##################################################################

# Action = Update foor by ID

@app.route('/foods/<int:id>', methods=['PUT'])
def update(id):
    #return "in update by ID for id "+ str(id)

    foundFoods = list(filter(lambda f: f['id'] == id, foods))
    if (len(foundFoods) == 0):
        abort(404)
    foundFood = foundFoods[0]

    if not request.json:
        abort(400)

    # Get what was passed up
    reqJson = request.json

    # Error checking - price a float - do later
    #if ('price' in reqJson and type(reqJson['price']) is not int):
    #    abort(400)

    # curl -i -H "Content-Type:application/json" -X PUT -d "{\"price\":4.80}" "http://127.0.0.1:5000/foods/3"
    # Info to update    
    if 'category' in reqJson:
        foundFood['category'] = reqJson['category']
    if 'name' in reqJson: 
        foundFood['name'] = reqJson['name']
    if 'price' in reqJson:
        foundFood['price'] = reqJson['price']

    return jsonify(foundFood)


# Action = Delete by ID
# curl -X DELETE "http://127.0.0.1:5000/foods/1"
@app.route('/foods/<int:id>', methods=['DELETE'])
def delete(id):
    #return "in delete by ID for id "+ str(id)

    #for each f in foods, check id until match
    foundFoods = list(filter(lambda f: f['id'] == id, foods))
    
    # Maybe print error message?
    if (len(foundFoods) == 0):
        abort(404)

    # Else remove the food by requested id
    foods.remove(foundFoods[0])
    return jsonify({"done":True})

##################################################################

if __name__ == '__main__' :
    app.run(debug= True)
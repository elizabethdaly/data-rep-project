#!flask/bin/python
from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

# List of acts (or a DB)
acts=[
    {"id": 1, "name":"Joe"},
    {"id": 2, "name":"Mary"}
]

# Keep track of ID as need to increment for new act
# This is a global var
nextId=3

# Action = Get all
# curl "http://127.0.0.1:5000/books"
@app.route('/acts')
def getAll():
    #return "in getAll"

    return jsonify(acts)

if __name__ == '__main__' :
    app.run(debug= True)
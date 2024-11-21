from flask import Flask, jsonify, request

# Creación del servidor
server = Flask(__name__)

@server.route("/", methods=["GET"])
def get_data():
    """
    Returns all data from the database
    """
    return "returns all data from the database"

@server.route("/<int:id>")
def get_one_by_id(id):
    """
    Returns a data from the database by id
    """
    return f"returns a data from the database by id = {id}"

@server.route("/", methods=["POST"])
def add_data():
    """
    Adds new data
    """
    return jsonify(request.json), 201

@server.route("/<int:id>", methods=["PATCH", "PUT"])
def modify_data(id):
    """
    Modifies existing data
    """
    return jsonify(request.json)

@server.route("/<int:id>", methods=["DELETE"])
def delete_data(id):
    """
    Deletes an item from the database
    """
    return f"delete an item from the data"

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=5000, debug=True)

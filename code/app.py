from flask import Flask, jsonify, request

app = Flask(__name__)
Stores = [
    {
        "name": "My store",
        "items": [
            {
                "name": "My item",
                "price": 15.09
            }
        ]
    }
]

@app.route("/store", methods = ['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        "name" : request_data['name'],   
        'items': []
    }
    Stores.append(new_store)
    return jsonify(new_store)


@app.route("/store/<string:name>")
def get_store(name):
    for store in Stores:
        if store['name'] == name:
            return jsonify(store)
    
    return jsonify({"message": "store not found"})


@app.route("/store/")
def get_stores():
    return jsonify({'Stores': Stores})

@app.route("/store/<string:name>/item", methods = ['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in Stores:
        if store['name'] == name:
            new_item = {
                "name" : request_data['name'],
                "price" : request_data['price']
            }
            store["items"].append(new_item)
            return jsonify(new_item)
    return jsonify({"message" : "store not found"})
    
@app.route("/store/<string:name>/item")
def get_item_in_store(name):
    for store in Stores:
        if store['name'] == name:
            return jsonify({"items": store['items']})
    return jsonify({"message": "item not found"})

app.run(port=3001)
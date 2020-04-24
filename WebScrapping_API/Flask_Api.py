from flask import Flask, jsonify, request

app = Flask(__name__)

stores = [
    {
        'name' : 'Prat Store',
        'items':
            [
                {
                  'name' :'Basket',
                  'price': 99.99
                }
            ]

    }
]

#Post - Receive the data
#GET - Used to send the data back only
#We programming the Web server......

'''POST/store data:(name:)
By Default GET request'''
@app.route('/store', methods=['POST'])
def create_store():
    request_data = request.get_json()
    new_store = {
        'name' : request_data['name'],
        'item' : []
    }

    stores.append(new_store)
    return  jsonify(new_store)


# GET/store/<string:name>
@app.route('/store/<string:name>')
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})


#iterate over the store
#if the store name matches return it
#If none mathch ,return an error message


# GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores})

# POST/ store/<string:name/item (name:price:)>
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name']  == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'Store not found'})


# GET / store/<string>:name/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message': 'store not found'})

app.run(debug=True,port=5000)





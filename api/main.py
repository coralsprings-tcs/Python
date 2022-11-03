from json import dumps
from flask import jsonify
from api.object import Item

def library():
    library = {}
    for i in range(1,11):
        item = Item(i,f'{i}-test',f'{i**2}').__dict__
        library[str(i)] = item
    return dumps(library)

def api():
    return jsonify(library())

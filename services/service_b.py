from model import BModel
from flask import jsonify

def hi():
    return "Hi from Service B", 200


def bye():
    return "Bye from Service B", 200


def get():
    try:
        db = BModel()
        row = db.get_data()
        ret = {'name': row[0]}
    except Exception as e:
        print(e)
        return '', 500

    return jsonify(ret)
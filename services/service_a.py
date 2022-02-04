from model import AModel
from flask import jsonify


def hi():
    return "Hi from Service A", 200


def bye():
    return "Bye from Service A", 200


def get():
    try:
        db = AModel()
        row = db.get_data()
        ret = {'name': row[0]}
    except Exception as e:
        print(e)
        return '', 500

    return jsonify(ret)

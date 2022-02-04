from flask import Blueprint
from services import service_b

bp = Blueprint("b", __name__, url_prefix="/b")


@bp.route('/hi', methods=['GET'])
def _hi():
    return service_b.hi()


@bp.route('/bye', methods=['GET'])
def _bye():
    return service_b.bye()


@bp.route('/get', methods=['GET'])
def _get():
    return service_b.get()
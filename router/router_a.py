from flask import Blueprint
from services import service_a

bp = Blueprint("a", __name__, url_prefix="/a")


@bp.route('/hi', methods=['GET'])
def _hi():
    return service_a.hi()


@bp.route('/bye', methods=['GET'])
def _bye():
    return service_a.bye()


@bp.route('/get', methods=['GET'])
def _get():
    return service_a.get()

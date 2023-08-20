from app.common.http_methods import GET, POST, PUT
from flask import Blueprint, jsonify, request
from .service import Service

from ..controllers import BeverageController

beverage = Blueprint('beverage', __name__)

service = Service(BeverageController)


@beverage.route('/', methods=POST)
def create_beverage():
    return service.create()


@beverage.route('/', methods=PUT)
def update_beverage():
    return service.update()


@beverage.route('/id/<_id>', methods=GET)
def get_beverage_by_id(_id: int):
    return service.get_by_id(_id=_id)


@beverage.route('/', methods=GET)
def get_beverages():
    return service.get_all()

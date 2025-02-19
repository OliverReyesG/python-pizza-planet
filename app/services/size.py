from app.common.http_methods import GET, POST, PUT
from flask import Blueprint
from .service import Service

from ..controllers import SizeController

size = Blueprint('size', __name__)

service = Service(SizeController)


@size.route('/', methods=POST)
def create_size():
    return service.create()


@size.route('/', methods=PUT)
def update_size():
    return service.update()


@size.route('/id/<_id>', methods=GET)
def get_size_by_id(_id: int):
    return service.get_by_id(_id=_id)


@size.route('/', methods=GET)
def get_sizes():
    return service.get_all()

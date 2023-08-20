from app.common.http_methods import GET, POST
from flask import Blueprint
from .service import Service

from ..controllers import OrderController

order = Blueprint('order', __name__)

service = Service(OrderController)


@order.route('/', methods=POST)
def create_order():
    return service.create()


@order.route('/id/<_id>', methods=GET)
def get_order_by_id(_id: int):
    return service.get_by_id(_id=_id)


@order.route('/', methods=GET)
def get_orders():
    return service.get_all()

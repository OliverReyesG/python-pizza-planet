from app.controllers import BaseController
from flask import jsonify, request


class Service:
    def __init__(self, controller: BaseController) -> None:
        self.controller = controller

    def create(self):
        entity, error = self.controller.create(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def update(self):
        entity, error = self.controller.update(request.json)
        response = entity if not error else {'error': error}
        status_code = 200 if not error else 400
        return jsonify(response), status_code

    def get_by_id(self, _id: int):
        entity, error = self.controller.get_by_id(_id)
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code

    def get_all(self):
        entity, error = self.controller.get_all()
        response = entity if not error else {'error': error}
        status_code = 200 if entity else 404 if not error else 400
        return jsonify(response), status_code

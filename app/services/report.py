from app.common.http_methods import GET, POST
from flask import Blueprint, jsonify, request

from ..controllers import ReportController

report = Blueprint('report', __name__)


@report.route('/', methods=GET)
def get_report():
    report, error = ReportController.get_report()
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/ingredient', methods=GET)
def get_most_requested_ingredient():
    report, error = ReportController.get_most_requested_ingredient()
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/revenue/month', methods=GET)
def get_revenue_by_month():
    report, error = ReportController.get_revenue_by_month()
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code


@report.route('/revenue/customer', methods=GET)
def get_revenue_by_customer():
    report, error = ReportController.get_revenue_by_customer()
    response = report if not error else {'error': error}
    status_code = 200 if report else 404 if not error else 400
    return jsonify(response), status_code

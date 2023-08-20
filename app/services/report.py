from app.common.http_methods import GET
from flask import Blueprint
from .service import Service

from ..controllers import ReportController


report = Blueprint('report', __name__)

service = Service(ReportController)


@report.route('/', methods=GET)
def get_report():
    return service.get_all()

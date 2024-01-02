from flask import Blueprint, request, jsonify

from src.main.adpters.request_adpter import request_adapter
from src.main.composers.patient_finder_composer import patient_finder_composer
from src.errors.error_handle import handle_errors

from src.main.services.decorator_service import token_required

patient_router_bp = Blueprint("patient_routes", __name__)


@patient_router_bp.route("/patients", methods=["GET"])
@token_required
def find_patient():
    http_response = None

    try:
        http_response = request_adapter(request, patient_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

from flask import Blueprint, request, jsonify

from src.main.adpters.request_adpter import request_adapter
from src.main.composers.pharmacie_finder_composer import pharmacie_finder_composer
from src.errors.error_handle import handle_errors

pharmacie_router_bp = Blueprint("pharmacie_routes", __name__)


@pharmacie_router_bp.route("/pharmacies", methods=["GET"])
def find_pharmacie():
    http_response = None

    try:
        http_response = request_adapter(request, pharmacie_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

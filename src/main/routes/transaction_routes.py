from flask import Blueprint, request, jsonify

from src.main.adpters.request_adpter import request_adapter
from src.main.composers.transaction_finder_composer import transaction_finder_composer
from src.errors.error_handle import handle_errors

from src.main.services.decorator_service import token_required

transaction_router_bp = Blueprint("transaction_routes", __name__)


@transaction_router_bp.route("/transactions", methods=["GET"])
@token_required
def find_transaction():
    http_response = None

    try:
        http_response = request_adapter(request, transaction_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

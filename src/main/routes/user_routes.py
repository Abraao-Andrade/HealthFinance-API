from flask import Blueprint, request, jsonify

from src.main.adpters.request_adpter import request_adapter

from src.main.composers.user_finder_composer import user_finder_composer
from src.main.composers.user_register_composer import user_register_composer
from src.main.composers.user_authenticate_composer import user_authenticate_composer

from src.errors.error_handle import handle_errors

from src.validators.user_register_validator import user_register_validator

user_router_bp = Blueprint("user_routes", __name__)


@user_router_bp.route("/user/auth", methods=["POST"])
def auth_user():
    http_response = None
    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_authenticate_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route("/user/find", methods=["GET"])
def find_user():
    http_response = None

    try:
        http_response = request_adapter(request, user_finder_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code


@user_router_bp.route("/user", methods=["POST"])
def register_user():
    http_response = None

    try:
        user_register_validator(request)
        http_response = request_adapter(request, user_register_composer())
    except Exception as exception:
        http_response = handle_errors(exception)

    return jsonify(http_response.body), http_response.status_code

from functools import wraps
from flask import request
from src.infra.db.repositories.users_repository import UsersRepository
from src.errors.types import HttpNotFoundError, HttpUnauthorizedError
from .auth_service import Authenticator


def token_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('Authorization')

        if not token:
            return {'message': 'Token de autenticação ausente'}, 401

        repository = UsersRepository()
        authenticator_service = Authenticator(repository)

        try:
            authenticator_service.validate_token(token)
        except HttpUnauthorizedError as e:
            return {'message': str(e)}, 401
        except HttpNotFoundError as e:
            return {'message': str(e)}, 404
        except Exception as e:
            return {'message': 'Erro interno do servidor'}, 500

        return f(*args, **kwargs)

    return decorated_function

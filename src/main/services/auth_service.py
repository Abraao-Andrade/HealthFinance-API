# pylint: disable=E0401:import-error, W0707:raise-missing-from
from datetime import datetime, timedelta
import jwt

from src.errors.types import HttpNotFoundError, HttpUnauthorizedError
from src.infra.db.repositories.users_repository import UsersRepository


class Authenticator:
    def __init__(self, use_case: UsersRepository, secret_key='4WeFWPcRjviuOdBNdqJDr8MFyawRKKaE'):
        self.secret_key = secret_key
        self.__use_case = use_case

    def generate_token(self, username):
        expiration_time = datetime.utcnow() + timedelta(seconds=3600)
        payload = {
            "username": username,
            "exp": expiration_time,
        }
        return jwt.encode(payload, self.secret_key, algorithm="HS256")

    def validate_token(self, token):
        try:
            token_data = jwt.decode(
                token, self.secret_key, algorithms=["HS256"])

            if not self.__use_case.select_user(token_data["username"]):
                raise HttpNotFoundError('Usuário não encontrado.')

        except jwt.ExpiredSignatureError:
            raise HttpUnauthorizedError('Token expirado')
        except jwt.InvalidTokenError:
            raise HttpUnauthorizedError('Token expirado')

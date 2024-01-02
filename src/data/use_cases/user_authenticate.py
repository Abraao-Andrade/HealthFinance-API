# pylint: disable=W0719:broad-exception-raised

from typing import Dict, List
from src.domain.use_cases.user_authenticate import UserAuthenticate as UserAuthenticateInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users
from src.infra.db.entities.users import Users as UsersEntity
from src.errors.types import HttpNotFoundError, HttpUnauthorizedError
from src.main.services.auth_service import Authenticator


class UserAuthenticate(UserAuthenticateInterface):
    def __init__(
            self, users_repository: UsersRepositoryInterface,
            authenticator: Authenticator) -> None:
        self.__users_repository = users_repository
        self.__authenticator = authenticator

    def authenticate(self, username: str, password: str) -> Dict:
        user = self.__search_user(username)

        self.__validate_password(user, password)

        token = self.__authenticator.generate_token(user.username)

        response = self.__format_response(user, token)

        return response

    @classmethod
    def __validate_password(cls, user: UsersEntity, password: str) -> None:
        if not user.check_password(password):
            raise HttpUnauthorizedError('Senha informada está incorreta.')

    def __search_user(self, username: str) -> List[Users]:
        users = self.__users_repository.select_user(username)
        if users == []:
            raise HttpNotFoundError('Usuario não encontrado.')
        return users[0]

    @classmethod
    def __format_response(cls, user: Users, token: str) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {'id': user.uuid, 'username': user.username, 'token': token}
        }

        return response

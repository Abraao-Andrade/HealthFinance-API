# pylint: disable=W0719:broad-exception-raised

import re
from typing import Dict, List
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, username: str) -> Dict:

        self.__validate_username(username)

        users = self.__search_user(username)
        response = self.__format_response(users)

        return response

    @classmethod
    def __validate_username(cls, username: str) -> None:
        # Expressão regular para verificar o formato básico de um email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, username):
            raise Exception('Email invalido para busca.')

    def __search_user(self, username: str) -> List[Users]:
        users = self.__users_repository.select_user(username)
        if users == []:
            raise Exception('Usuario nao encontrado.')
        return users

    @classmethod
    def __format_response(cls, users: List[Users]) -> Dict:
        attributes = []

        for user in users:
            attributes.append(
                {'id': user.uuid, 'username': user.username}
            )

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": attributes
        }

        return response

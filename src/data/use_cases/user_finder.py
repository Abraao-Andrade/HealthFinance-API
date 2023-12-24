# pylint: disable=W0719:broad-exception-raised

import re
from typing import Dict
from src.domain.use_cases.user_finder import UserFinder as UserFinderInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserFinder(UserFinderInterface):
    def __init__(self, users_repository: UsersRepositoryInterface) -> None:
        self.__users_repository = users_repository

    def find(self, username: str) -> Dict:
        # Expressão regular para verificar o formato básico de um email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, username):
            raise Exception('Email invalido para busca.')

        users = self.__users_repository.select_user(username)
        if users == []:
            raise Exception('Usuario nao encontrado.')

        response = {
            "type": "Users",
            "count": len(users),
            "attributes": users
        }

        return response

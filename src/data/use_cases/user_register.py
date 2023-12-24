# pylint: disable=W0719:broad-exception-raised, W0622:redefined-builtin

import re
from uuid import UUID
from typing import Dict
from src.domain.use_cases.user_register import UserRegister as UserRegisterInterface
from src.data.interfaces.users_repository import UsersRepositoryInterface


class UserRegister(UserRegisterInterface):

    def __init__(self, user_repository: UsersRepositoryInterface) -> None:
        self.__user_repository = user_repository

    def register(self, username: str, password: str) -> Dict:
        self.__validate_username(username)
        self.__register_user_data(username, password)

        response = self.__format_response(username, password)
        return response

    @classmethod
    def __validate_username(cls, username: str) -> None:
        # Expressão regular para verificar o formato básico de um email
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if not re.match(pattern, username):
            raise Exception('Email invalido para cadastro.')

    def __register_user_data(self, username: str, password: str) -> None:
        self.__user_repository.insert_user(username, password)

    @classmethod
    def __format_response(cls, username: str, id: UUID) -> Dict:
        response = {
            "type": "Users",
            "count": 1,
            "attributes": {
                'id': id,
                'username': username
            }
        }

        return response

from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity
from src.data.interfaces.users_repository import UsersRepositoryInterface
from src.domain.models.users import Users


class UsersRepository(UsersRepositoryInterface):

    @classmethod
    def insert_user(cls, username: str, password: str) -> None:
        with DBConnectionHandler() as database:
            try:
                new_registry = UserEntity(username=username)
                new_registry.set_password(password)

                database.session.add(new_registry)
                database.session.commit()
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_user(cls, username: str) -> List[Users]:
        with DBConnectionHandler() as database:
            try:
                users = (
                    database.session.query(UserEntity)
                    .filter(UserEntity.username == username)
                    .all()
                )
                return users
            except Exception as exception:
                database.session.rollback()
                raise exception

from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.users import Users as UserEntity


class UsersRepository:

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

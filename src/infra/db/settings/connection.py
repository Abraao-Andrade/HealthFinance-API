from sqlalchemy import create_engine


class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_string = "{}:///{}/{}".format(
            'sqlite',
            'init',
            'backend_test.db',
        )
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine

    def get_engine(self):
        return self.__engine

from typing import List
from abc import ABC, abstractmethod
from src.domain.models.users import Users


class UsersRepositoryInterface(ABC):

    @abstractmethod
    def insert_user(self, username: str, password: str) -> None: pass

    @abstractmethod
    def select_user(self, username: str) -> List[Users]: pass

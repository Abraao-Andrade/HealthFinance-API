from abc import ABC, abstractmethod
from typing import Dict


class UserRegister(ABC):

    @abstractmethod
    def register(self, username: str, password: str) -> Dict: pass

from abc import ABC, abstractmethod
from typing import Dict


class UserAuthenticate(ABC):

    @abstractmethod
    def authenticate(self, username: str, password: str) -> Dict: pass

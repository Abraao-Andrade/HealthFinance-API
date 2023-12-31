from abc import ABC, abstractmethod
from typing import Dict


class PatientFinder(ABC):

    @abstractmethod
    def find(self, first_name: str) -> Dict: pass

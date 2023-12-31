# pylint: disable=W0719:broad-exception-raised
from typing import Dict, List, Optional
from src.domain.use_cases.pharmacie_finder import PharmacieFinder as PharmacieFinderInterface
from src.data.interfaces.pharmacies_repository import PharmaciesRepositoryInterface
from src.domain.models.pharmacies import Pharmacies
from src.errors.types import HttpBadRequestError, HttpNotFoundError


class PharmacieFinder(PharmacieFinderInterface):
    def __init__(self, pharmacie_repository: PharmaciesRepositoryInterface) -> None:
        self.__pharmacies_repository = pharmacie_repository

    def find(self, name: Optional[str] = None) -> Dict:

        if name:
            self.__validate_name(name)

        pharmacies = self.__search_pharmacie(name)
        response = self.__format_response(pharmacies)

        return response

    @classmethod
    def __validate_name(cls, name: str) -> None:
        name_without_spaces = "".join(name.split())
        if not name_without_spaces.isalpha():
            raise HttpBadRequestError('Nome invalido para a busca')

        if len(name_without_spaces) > 18:
            raise HttpBadRequestError('Nome muito grande para busca')

    def __search_pharmacie(self, name: Optional[str] = None) -> List[Pharmacies]:
        pharmacies = []

        if name:
            pharmacies = self.__pharmacies_repository.select_pharmacie(name)
        else:
            pharmacies = self.__pharmacies_repository.select_all_pharmacies()

        if pharmacies == []:
            raise HttpNotFoundError('Farmacia não encontrada.')
        return pharmacies

    @classmethod
    def __format_response(cls, pharmacies: List[Pharmacies]) -> Dict:
        attributes = []

        for pharmacie in pharmacies:
            attributes.append(
                {'id': pharmacie.uuid, 'name': pharmacie.name, 'city': pharmacie.city}
            )

        response = {
            "type": "Pharmacies",
            "count": len(pharmacies),
            "attributes": attributes
        }

        return response

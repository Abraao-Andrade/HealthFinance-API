from typing import List
from src.infra.db.settings.connection import DBConnectionHandler
from src.infra.db.entities.pharmacies import Pharmacies as PharmaciesEntity
from src.data.interfaces.pharmacies_repository import PharmaciesRepositoryInterface
from src.domain.models.pharmacies import Pharmacies


class PharmaciesRepository(PharmaciesRepositoryInterface):

    @classmethod
    def select_pharmacie(cls, name: str) -> List[Pharmacies]:
        with DBConnectionHandler() as database:
            try:
                patients = (
                    database.session.query(PharmaciesEntity)
                    .filter(PharmaciesEntity.name == name)
                    .all()
                )
                return patients
            except Exception as exception:
                database.session.rollback()
                raise exception

    @classmethod
    def select_all_pharmacies(cls) -> List[Pharmacies]:
        with DBConnectionHandler() as database:
            try:
                patients = (
                    database.session.query(PharmaciesEntity)
                    .all()
                )
                return patients
            except Exception as exception:
                database.session.rollback()
                raise exception

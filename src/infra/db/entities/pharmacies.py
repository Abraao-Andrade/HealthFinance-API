# pylint: disable=E0401:import-error

from sqlalchemy import Column, String
from src.infra.db.settings.base import Base


class Pharmacies(Base):
    __tablename__ = "PHARMACIES"

    uuid = Column(String, primary_key=True)
    name = Column(String, nullable=False)
    city = Column(String, nullable=False)

    def __repr__(self):
        return f"Pharmacies [uuid={self.uuid}, name={self.name}, city={self.city}]"

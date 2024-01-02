# pylint: disable=R0913: too-many-arguments
from datetime import datetime


class Transactions:
    def __init__(
        self,
        uuid: str,
        patient_uuid: str,
        pharmacy_uuid: str,
        amount: float,
        timestamp: datetime
    ) -> None:
        self.uuid = uuid
        self.patient_uuid = patient_uuid
        self.pharmacy_uuid = pharmacy_uuid
        self.amount = amount
        self.timestamp = timestamp

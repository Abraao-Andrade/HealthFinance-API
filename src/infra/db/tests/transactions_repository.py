import uuid as uuid_lib
from typing import List
from src.domain.models.transactions import Transactions


class TransactionsRepositorySpy:

    def __init__(self) -> None:
        self.select_transaction_attributes = {}

    def select_transaction(self, uuid: str) -> List[Transactions]:
        self.select_transaction_attributes["uuid"] = uuid
        return [
            Transactions(
                uuid_lib.uuid4,
                "UUID(PATIENT)",
                "UUID(PHARMACIE)",
                120.0,
                "1996-10-25 00:00:00.000000",
            ),
        ]

    def select_all_transactions(self) -> List[Transactions]:
        return [
            Transactions(
                uuid_lib.uuid4,
                "UUID(PATIENT)",
                "UUID(PHARMACIE)",
                120.0,
                "1996-10-25 00:00:00.000000",
            ),
            Transactions(
                uuid_lib.uuid4,
                "UUID(PATIENT01)",
                "UUID(PHARMACIE01)",
                125.0,
                "1996-10-26 00:00:00.000000",
            ),
        ]

    def select_pharmacy_transactions(self, pharmacy_uuid: str) -> List[Transactions]:
        self.select_transaction_attributes["pharmacy_uuid"] = pharmacy_uuid
        return [
            Transactions(
                uuid_lib.uuid4,
                "UUID(PATIENT)",
                pharmacy_uuid,
                120.0,
                "1996-10-25 00:00:00.000000",
            ),
        ]

    def select_patient_transactions(self, patient_uuid: str) -> List[Transactions]:
        self.select_transaction_attributes["patient_uuid"] = patient_uuid
        return [
            Transactions(
                uuid_lib.uuid4,
                "UUID(PATIENT)",
                patient_uuid,
                120.0,
                "1996-10-25 00:00:00.000000",
            ),
        ]

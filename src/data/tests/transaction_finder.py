from typing import Dict


class TransactionFinderSpy:
    def __init__(self) -> None:
        self.find_attributes = {}

    def find(self, uuid: str) -> Dict:
        self.find_attributes["uuid"] = uuid

        return {
            "type": "Transactions",
            "count": 1,
            "attributes": [
                {
                    'id': "UUID(abscld-dr12345-shfg)",
                    'patient_uuid': "UUID(PATIENT)",
                    'pharmacy_uuid': "UUID(PHARMACIE)",
                    'amount': 120.0,
                    'timestamp': "1996-10-25 00:00:00.000000",
                }
            ]
        }

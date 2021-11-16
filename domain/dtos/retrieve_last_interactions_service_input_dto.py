from dataclasses import dataclass


@dataclass
class RetrieveLastInteractionsServiceInputDTO:
    user_id: str
    amount: int

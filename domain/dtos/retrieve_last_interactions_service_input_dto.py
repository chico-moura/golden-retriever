from dataclasses import dataclass

from domain.value_objects import UserAccount


@dataclass
class RetrieveLastInteractionsServiceInputDTO:
    user_id: str
    user_token: str
    amount: int

    @property
    def user_account(self) -> UserAccount:
        return UserAccount(
            id=self.user_id,
            token=self.user_token
        )

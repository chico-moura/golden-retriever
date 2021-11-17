from abc import ABC, abstractmethod
from typing import List

from domain.entities import Interaction
from domain.value_objects.user_account import UserAccount


class InteractionRepository(ABC):
    @abstractmethod
    def fetch_last_interactions(self, user_account: UserAccount, amount: int) -> List[Interaction]:
        pass

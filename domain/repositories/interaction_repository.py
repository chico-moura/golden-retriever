from abc import ABC, abstractmethod
from typing import List

from domain.entities import Interaction
from domain.value_objects.user_id import UserID


class InteractionRepository(ABC):
    @abstractmethod
    def fetch_last_interactions(self, user_id: UserID, amount: int) -> List[Interaction]:
        pass

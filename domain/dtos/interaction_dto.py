from dataclasses import dataclass
from datetime import datetime

from domain.entities import Interaction


@dataclass(frozen=True)
class InteractionDTO:
    time_stamp: datetime
    description: str

    def from_entity(self) -> Interaction:
        pass

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from domain.entities import Interaction
from domain.factories import InteractionFactory


@dataclass(frozen=True)
class InteractionDTO:
    time_stamp: datetime
    description: str

    @classmethod
    def from_entity(cls, interaction: Interaction) -> InteractionDTO:
        return cls(
            time_stamp=interaction.time_stamp.value,
            description=interaction.description.value
        )

    def to_entity(self) -> Interaction:
        return InteractionFactory.build(
            time_stamp=self.time_stamp,
            description=self.description
        )

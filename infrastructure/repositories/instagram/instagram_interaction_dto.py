from dateutil import parser
from dataclasses import dataclass

from domain.entities import Interaction
from domain.factories import InteractionFactory


@dataclass(frozen=True)
class InstagramInteractionDTO:
    id: str
    timestamp: str
    media_type: str

    def to_entity(self) -> Interaction:
        time_stamp = parser.parse(self.timestamp)

        return InteractionFactory.build(
            time_stamp=time_stamp,
            description=self.media_type
        )

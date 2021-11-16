from datetime import datetime

from domain.entities import Interaction
from domain.value_objects import InteractionTimeStamp, InteractionDescription


class InteractionFactory:
    @staticmethod
    def build(
        time_stamp: datetime,
        description: str
    ) -> Interaction:
        return Interaction(
            time_stamp=InteractionTimeStamp(time_stamp),
            description=InteractionDescription(description)
        )

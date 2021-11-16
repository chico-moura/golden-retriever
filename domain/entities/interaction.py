from dataclasses import dataclass

from domain.value_objects import InteractionDescription
from domain.value_objects import InteractionTimeStamp


@dataclass
class Interaction:
    time_stamp: InteractionTimeStamp
    description: InteractionDescription

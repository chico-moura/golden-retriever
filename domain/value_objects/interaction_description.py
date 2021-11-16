from dataclasses import dataclass


@dataclass(frozen=True)
class InteractionDescription:
    value: str

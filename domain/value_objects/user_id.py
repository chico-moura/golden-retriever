from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class UserID(ABC):
    value: str

    @abstractmethod
    def __validate(self) -> None:
        pass

    def __post_init__(self) -> None:
        self.__validate()

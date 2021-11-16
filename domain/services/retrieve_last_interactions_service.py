from typing import List

from domain.dtos import RetrieveLastInteractionsServiceInputDTO, InteractionDTO
from domain.repositories import InteractionRepository
from domain.value_objects import UserID


class RetrieveLastInteractionsService:
    __interaction_repository: InteractionRepository

    def __init__(self, interaction_repository: InteractionRepository) -> None:
        self.__interaction_repository = interaction_repository

    def execute(self, input_dto: RetrieveLastInteractionsServiceInputDTO) -> List[InteractionDTO]:
        user_id = UserID(value=input_dto.user_id)
        interactions = self.__interaction_repository.fetch_last_interactions(
            user_id=user_id,
            amount=input_dto.amount
        )
        return list(map(InteractionDTO.from_entity, interactions))

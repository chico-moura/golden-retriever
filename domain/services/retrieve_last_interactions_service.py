from typing import List

from domain.dtos import RetrieveLastInteractionsServiceInputDTO, InteractionDTO
from domain.repositories import InteractionRepository
from domain.value_objects import UserAccount


class RetrieveLastInteractionsService:
    __interaction_repository: InteractionRepository

    def __init__(self, interaction_repository: InteractionRepository) -> None:
        self.__interaction_repository = interaction_repository

    def execute(self, input_dto: RetrieveLastInteractionsServiceInputDTO) -> List[InteractionDTO]:
        user_account = UserAccount(
            id=input_dto.user_id,
            token=input_dto.user_token
        )
        interactions = self.__interaction_repository.fetch_last_interactions(
            user_account=user_account,
            amount=input_dto.amount
        )
        return list(map(InteractionDTO.from_entity, interactions))

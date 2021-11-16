from unittest import TestCase

from mockito import mock, unstub, when, verify
from testfixtures import compare

from domain.dtos import RetrieveLastInteractionsServiceInputDTO, InteractionDTO
from domain.repositories import InteractionRepository
from domain.services.retrieve_last_interactions_service import RetrieveLastInteractionsService
from domain.tests.test_factories import InteractionTestFactory, RetrieveLastInteractionsServiceInputDTOTestFactory
from domain.value_objects import UserID


class TestRetrieveLastInteractionService(TestCase):
    def setUp(self) -> None:
        self.interaction_repository = mock(InteractionRepository)
        self.retrieve_last_interactions_service = RetrieveLastInteractionsService(self.interaction_repository)
        self.input_dto: RetrieveLastInteractionsServiceInputDTO = RetrieveLastInteractionsServiceInputDTOTestFactory.build()

    def tearDown(self) -> None:
        unstub()

    def test_execute_WHEN_called_THEN_calls_interaction_repository_get_last_interactions_with_given_arguments(self) -> None:
        user_id = UserID(self.input_dto.user_id)
        when(self.interaction_repository).fetch_last_interactions(
            user_id=user_id,
            amount=self.input_dto.amount
        ).thenReturn([])

        self.retrieve_last_interactions_service.execute(self.input_dto)

        verify(self.interaction_repository).fetch_last_interactions(
            user_id=user_id,
            amount=self.input_dto.amount
        )

    def test_execute_WHEN_called_THEN_returns_interaction_dtos_from_interactions_returned_by_repository(self) -> None:
        fetched_interactions = InteractionTestFactory.build_batch(size=2)
        when(self.interaction_repository).fetch_last_interactions(...).thenReturn(fetched_interactions)

        result_interaction_dtos = self.retrieve_last_interactions_service.execute(self.input_dto)

        expected_interaction_dtos = [
            InteractionDTO(
                time_stamp=interaction.time_stamp.value,
                description=interaction.description.value
            )
            for interaction in fetched_interactions
        ]
        compare(expected_interaction_dtos, result_interaction_dtos)

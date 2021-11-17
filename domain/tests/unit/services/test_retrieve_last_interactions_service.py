from unittest import TestCase

from mockito import mock, unstub, when, verify
from testfixtures import compare

from domain.dtos import RetrieveLastInteractionsServiceInputDTO, InteractionDTO
from domain.repositories import InteractionRepository
from domain.services.retrieve_last_interactions_service import RetrieveLastInteractionsService
from domain.tests.test_factories import InteractionTestFactory, RetrieveLastInteractionsServiceInputDTOTestFactory
from domain.tests.test_factories.user_account_test_factory import UserAccountTestFactory
from domain.value_objects import UserAccount


class TestRetrieveLastInteractionService(TestCase):
    def setUp(self) -> None:
        self.interaction_repository = mock(InteractionRepository)
        self.retrieve_last_interactions_service = RetrieveLastInteractionsService(self.interaction_repository)
        self.user_account: UserAccount = UserAccountTestFactory.build()
        self.input_dto: RetrieveLastInteractionsServiceInputDTO = RetrieveLastInteractionsServiceInputDTOTestFactory.build(
            user_id=self.user_account.id,
            user_token=self.user_account.token
        )

    def tearDown(self) -> None:
        unstub()

    def test_execute_WHEN_called_THEN_calls_interaction_repository_get_last_interactions_with_given_arguments(self) -> None:
        when(self.interaction_repository).fetch_last_interactions(
            user_account=self.user_account,
            amount=self.input_dto.amount
        ).thenReturn([])

        self.retrieve_last_interactions_service.execute(self.input_dto)

        verify(self.interaction_repository).fetch_last_interactions(
            user_account=self.user_account,
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

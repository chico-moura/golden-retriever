from unittest import TestCase

import tokens
from domain.entities import Interaction
from domain.value_objects import UserAccount
from infrastructure.repositories.instagram.instagram_interaction_repository import InstagramInteractionRepository


class TestInstagramInteractionRepository(TestCase):
    def test_fetch_last_interactions_WHEN_called_THEN_returns_interactions(self) -> None:
        instagram_interaction_repository = InstagramInteractionRepository()
        user_account = UserAccount(
            id='',
            token=tokens.INSTAGRAM_ACCESS_TOKEN
        )

        result_interactions = instagram_interaction_repository.fetch_last_interactions(
            user_account=user_account,
            amount=1
        )

        self.assertIsInstance(result_interactions[0], Interaction)

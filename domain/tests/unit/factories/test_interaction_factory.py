from unittest import TestCase

from testfixtures import compare

from domain.entities import Interaction
from domain.factories.interaction_factory import InteractionFactory
from domain.tests.test_factories import InteractionTestFactory


class TestInteractionFactory(TestCase):
    def test_build_WHEN_called_THEN_returns_interaction(self) -> None:
        expected_interaction: Interaction = InteractionTestFactory.build()

        result_interaction = InteractionFactory.build(
            time_stamp=expected_interaction.time_stamp.value,
            description=expected_interaction.description.value
        )

        compare(expected_interaction, result_interaction)

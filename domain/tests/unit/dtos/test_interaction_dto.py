from unittest import TestCase

from testfixtures import compare

from domain.dtos import InteractionDTO
from domain.entities import Interaction
from domain.tests.test_factories import InteractionTestFactory, InteractionDTOTestFactory
from domain.value_objects import InteractionTimeStamp, InteractionDescription


class TestInteractionDTO(TestCase):
    def test_from_entity_WHEN_called_THEN_returns_interaction_dto(self) -> None:
        interaction: Interaction = InteractionTestFactory.build()

        result_interaction_dto = InteractionDTO.from_entity(interaction)

        expected_interaction_dto = InteractionDTO(
            time_stamp=interaction.time_stamp.value,
            description=interaction.description.value
        )
        compare(expected_interaction_dto, result_interaction_dto)

    def test_to_entity_WHEN_called_THEN_returns_interaction(self) -> None:
        interaction_dto: InteractionDTO = InteractionDTOTestFactory.build()

        result_interaction = interaction_dto.to_entity()

        expected_interaction = Interaction(
            InteractionTimeStamp(interaction_dto.time_stamp),
            InteractionDescription(interaction_dto.description)
        )
        compare(expected_interaction, result_interaction)

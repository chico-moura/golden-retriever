from datetime import datetime
from unittest import TestCase

from infrastructure.repositories.instagram.instagram_interaction_dto import InstagramInteractionDTO


class TestInstagramInteractionDTO(TestCase):
    def test_to_entity_WHEN_timestamp_is_ISO_8601_THEN_returns_assigns_correct_hour(self) -> None:
        instagram_interaction_dto = InstagramInteractionDTO(
            id='',
            timestamp='2020-11-22T19:22:08+0000',
            media_type='IMAGE'
        )

        result_interaction = instagram_interaction_dto.to_entity()

        expected_time_stamp = datetime(2020, 11, 22, 19, 22, 8).hour
        self.assertEqual(expected_time_stamp, result_interaction.time_stamp.value.hour)

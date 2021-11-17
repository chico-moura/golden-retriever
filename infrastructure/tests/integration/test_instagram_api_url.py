from unittest import TestCase

import requests

import tokens
from domain.value_objects import UserAccount
from infrastructure.repositories.instagram.instagram_api_url import InstagramAPIURL


class TestInstagramAPIURL(TestCase):
    def test_medias_WHEN_get_request_send_THEN_returns_status_200(self) -> None:
        user_account = UserAccount(
            id='',
            token=tokens.INSTAGRAM_ACCESS_TOKEN
        )
        url = InstagramAPIURL.medias(user_account)

        response = requests.get(url)
        expected_status = 200
        self.assertEqual(expected_status, response.status_code)

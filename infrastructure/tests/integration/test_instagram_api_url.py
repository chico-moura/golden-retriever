from unittest import TestCase

import requests

from infrastructure.repositories.instagram.instagram_api_url import InstagramAPIURL


class TestInstagramAPIURL(TestCase):
    def test_medias_WHEN_get_request_send_THEN_returns_status_200(self) -> None:
        url = InstagramAPIURL.medias()

        response = requests.get(url)
        expected_status = 200
        self.assertEqual(expected_status, response.status_code)

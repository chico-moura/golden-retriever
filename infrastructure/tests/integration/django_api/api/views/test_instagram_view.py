from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from testfixtures import compare


class TestInstagramView(APITestCase):
    def setUp(self) -> None:
        self.url = reverse('instagram')

    def test_get_WHEN_request_received_THEN_returns_status_code_200(self) -> None:
        response = self.client.get(self.url)

        expected_status = status.HTTP_200_OK
        self.assertEqual(expected_status, response.status_code)

    def test_get_WHEN_request_received_THEN_returns_payload(self) -> None:
        response = self.client.get(self.url)

        expected_keys = ['time_stamp', 'description']
        sample_interaction = response.json()[0]
        compare(expected_keys, sample_interaction.keys())

    def test_get_WHEN_amount_provided_THEN_returns_amount_of_data(self) -> None:
        expected_amount = 3
        url = self.url + f'?amount={expected_amount}'

        response = self.client.get(url)

        payload = response.json()
        self.assertEqual(expected_amount, len(payload))


import requests
from typing import List, Dict

from domain.entities import Interaction
from domain.repositories import InteractionRepository
from domain.value_objects import UserAccount
from infrastructure.repositories.instagram.instagram_api_url import InstagramAPIURL
from infrastructure.repositories.instagram.instagram_interaction_dto import InstagramInteractionDTO


class InstagramInteractionRepository(InteractionRepository):
    def fetch_last_interactions(self, user_account: UserAccount, amount: int) -> List[Interaction]:
        url = InstagramAPIURL.medias(user_account)
        response = requests.get(url)
        data_set = self.__fetch_data_from_response(
            response=response,
            amount=amount
        )

        return [InstagramInteractionDTO(**data).to_entity() for data in data_set]

    @staticmethod
    def __fetch_data_from_response(response: requests.Response, amount: int) -> List[Dict]:
        json = response.json()
        data = json['data']
        return data[:amount]

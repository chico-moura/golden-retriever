from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from infrastructure.django_api.api.serializers.interaction_dto_serializer import InteractionDTOSerializer
from tokens import INSTAGRAM_ACCESS_TOKEN
from domain.dtos import RetrieveLastInteractionsServiceInputDTO
from domain.services import RetrieveLastInteractionsService
from infrastructure.repositories.instagram.instagram_interaction_repository import InstagramInteractionRepository


class InstagramView(APIView):
    __retrieve_last_interactions_service: RetrieveLastInteractionsService

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        instagram_interaction_repository = InstagramInteractionRepository()
        self.__retrieve_last_interactions_service = RetrieveLastInteractionsService(instagram_interaction_repository)

    def get(self, request: Request) -> Response:
        amount = self.__get_amount_from_request(request)
        retrieve_last_interactions_service_input_dto = RetrieveLastInteractionsServiceInputDTO(
            user_id='',
            user_token=INSTAGRAM_ACCESS_TOKEN,
            amount=amount
        )

        interaction_dtos = self.__retrieve_last_interactions_service.execute(retrieve_last_interactions_service_input_dto)

        serializer = InteractionDTOSerializer(interaction_dtos, many=True)
        return Response(
            data=serializer.data,
            status=status.HTTP_200_OK
        )

    @staticmethod
    def __get_amount_from_request(request: Request) -> int:
        default_amount = 10
        amount = request.query_params.get('amount', default_amount)
        return int(amount)

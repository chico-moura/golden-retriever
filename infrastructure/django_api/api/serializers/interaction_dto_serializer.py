from rest_framework_dataclasses.serializers import DataclassSerializer

from domain.dtos import InteractionDTO


class InteractionDTOSerializer(DataclassSerializer):
    class Meta:
        dataclass = InteractionDTO

from factory import Factory, Faker

from domain.dtos import InteractionDTO


class InteractionDTOTestFactory(Factory):
    class Meta:
        model = InteractionDTO

    time_stamp = Faker('date_time')
    description = Faker('text')

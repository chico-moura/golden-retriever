from factory import Factory, Faker

from domain.dtos import RetrieveLastInteractionsServiceInputDTO


class RetrieveLastInteractionsServiceInputDTOTestFactory(Factory):
    class Meta:
        model = RetrieveLastInteractionsServiceInputDTO

    user_id = Faker('uuid4')
    user_token = Faker('uuid4')
    amount = Faker('random_int', min=2, max=4)

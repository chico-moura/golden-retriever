from factory import Factory, Faker

from domain.dtos import RetrieveLastInteractionsServiceInputDTO


class RetrieveLastInteractionsServiceInputDTOTestFactory(Factory):
    class Meta:
        model = RetrieveLastInteractionsServiceInputDTO

    user_id = Faker('email')
    amount = Faker('random_int', min=2, max=4)

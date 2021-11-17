from factory import Factory, Faker

from domain.value_objects import UserAccount


class UserAccountTestFactory(Factory):
    class Meta:
        model = UserAccount

    id = Faker('uuid4')
    token = Faker('uuid4')

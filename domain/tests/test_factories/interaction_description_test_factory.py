from factory import Factory, Faker

from domain.value_objects import InteractionDescription


class InteractionDescriptionTestFactory(Factory):
    class Meta:
        model = InteractionDescription

    value = Faker('text')

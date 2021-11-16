from factory import Factory, Faker

from domain.value_objects import InteractionTimeStamp


class InteractionTimeStampTestFactory(Factory):
    class Meta:
        model = InteractionTimeStamp

    value = Faker('datetime_object')

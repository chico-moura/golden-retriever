from factory import Factory, SubFactory

from domain.entities import Interaction
from domain.tests.test_factories import InteractionTimeStampTestFactory, InteractionDescriptionTestFactory


class InteractionTestFactory(Factory):
    class Meta:
        model = Interaction

    time_stamp = SubFactory(InteractionTimeStampTestFactory)
    description = SubFactory(InteractionDescriptionTestFactory)

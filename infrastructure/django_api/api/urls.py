from django.urls import path

from infrastructure.django_api.api.views.instagram_view import InstagramView

urlpatterns = [
    path('instagram', InstagramView.as_view(), name='instagram')
]

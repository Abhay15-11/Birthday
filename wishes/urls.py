from django.urls import path
from .views import birthday_card

urlpatterns = [
    path('', birthday_card, name='birthday_card'),
]

from django.urls import path
from .views import CardView, card_create, card_list


urlpatterns = [
    path('cards/', CardView.as_view(), name='card'),
    path('create/card/', card_create, name='card_create'),
    path('list/card/', card_list, name='card_list'),
]

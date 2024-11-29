from django.urls import path
from .views import CardView, UserLoginView, CorrectView, card_create, card_list


urlpatterns = [
    path('cards/', CardView.as_view()),
    path('login/', UserLoginView.as_view()),
    path('analiz/', CorrectView.as_view()),
    path('create/card/', card_create),
    path('list/card/', card_list),
]

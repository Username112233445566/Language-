from django.urls import path
from .views import (
    RegisterTemplateView,
    LoginTemplateView,
    CardCreateTemplateView,
    RegisterView,
    CardListView,
    CardListTemplateView,
)

urlpatterns = [
    path('reg/', RegisterView.as_view(), name='register'),
    path('cards/', CardListView.as_view(), name='card_list'),

    path('login/', LoginTemplateView.as_view(), name='login_template'),
    path('register/', RegisterTemplateView.as_view(), name='register_template'),

    path('cards_list/', CardListTemplateView.as_view(), name='card_list'),
    path('cards_create/', CardCreateTemplateView.as_view(), name='cards_list_template'),
]
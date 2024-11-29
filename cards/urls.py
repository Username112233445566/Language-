from django.urls import path
from .views import (
    RegisterTemplateView,
    LoginTemplateView,
    CardListTemplateView,
    CardDetailTemplateView,
    RegisterView,
    CardListView,
    CardDetailView,
)

urlpatterns = [
    # Карточки
    path('cards/', CardListView.as_view(), name='card_list'),
    path('cards/<int:pk>/', CardDetailView.as_view(), name='card_detail'),

    path('register/', RegisterTemplateView.as_view(), name='register_template'),
    path('login/', LoginTemplateView.as_view(), name='login_template'),
    path('cards_list/', CardListTemplateView.as_view(), name='cards_list_template'),
    path('card/<int:pk>/', CardDetailTemplateView.as_view(), name='card_detail_template'),
]

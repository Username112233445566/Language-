from rest_framework import generics
from django.shortcuts import render
from .models import Card, User, Correct
from .serializers import CardSerializer, UserSerializer, CorrectSerializer
from django.http import JsonResponse

class CardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class UserLoginView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CorrectView(generics.UpdateAPIView):
    queryset = Correct.objects.all()
    serializer_class = CorrectSerializer


def card_create(request):
    return render(request, 'create_card.html') 

def card_list(request):
    return render(request, 'card_list.html') 
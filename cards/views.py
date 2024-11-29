from rest_framework import generics
from django.shortcuts import render
from .models import Card
from .serializers import CardSerializer
from django.http import JsonResponse

class CardView(generics.ListCreateAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

def card_create(request):
    return render(request, 'create_card.html') 

def card_list(request):
    return render(request, 'card_list.html') 
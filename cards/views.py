from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Card
from .serializers import CardSerializer, UserSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardListView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Card.objects.all()
    serializer_class = CardSerializer


class RegisterTemplateView(APIView):
    def get(self, request):
        return render(request, 'register.html')


class LoginTemplateView(APIView):
    def get(self, request):
        return render(request, 'login.html')


class CardListTemplateView(APIView):
    def get(self, request):
        return render(request, 'cards.html')
    

class CardCreateTemplateView(APIView):
    def get(self, request):
        return render(request, 'create_card.html')
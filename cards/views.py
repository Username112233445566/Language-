from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render
from .models import Card
from .serializers import CardSerializer, UserSerializer, CorrectSerializer


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CardListView(generics.ListAPIView):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsAuthenticated]  # Только для аутентифицированных пользователей


class CardDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            card = Card.objects.get(pk=pk)
            return Response({
                "word": card.word,
                "translation": card.translation,
                "example": card.example,
            })
        except Card.DoesNotExist:
            return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk):
        try:
            card = Card.objects.get(pk=pk)
            is_correct = request.data.get("is_correct", False)

            # Обновляем статистику пользователя
            correct = request.user.correct
            if is_correct:
                correct.last_correct = correct.correct
                correct.correct += 1
            else:
                correct.last_correct = correct.correct
            correct.save()

            return Response({"message": "Answer recorded"})
        except Card.DoesNotExist:
            return Response({"error": "Card not found"}, status=status.HTTP_404_NOT_FOUND)

# Шаблон регистрации
class RegisterTemplateView(APIView):
    def get(self, request):
        return render(request, 'register.html')


# Шаблон входа
class LoginTemplateView(APIView):
    def get(self, request):
        return render(request, 'login.html')


# Шаблон списка карточек
class CardListTemplateView(APIView):
    def get(self, request):
        return render(request, 'cards_list.html')


# Шаблон карточки
class CardDetailTemplateView(APIView):
    def get(self, request, pk):
        return render(request, 'card_detail.html', {'card_id': pk})
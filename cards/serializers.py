from rest_framework import serializers
from .models import Card, User, Correct

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'star': {'required': False},
        }

class CorrectSerializer(serializers.Serializer):
    class Meta:
        model = Correct
        fields = '__all__'
        extra_kwargs = {
            'correct': {'required': False},
            'last_correct': {'required': False},
        }
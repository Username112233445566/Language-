from rest_framework import serializers
from .models import Card, Correct
from django.contrib.auth.models import User

class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password']
        )
        Correct.objects.create(user=user)
        return user

class CorrectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Correct
        fields = ['last_correct', 'correct']

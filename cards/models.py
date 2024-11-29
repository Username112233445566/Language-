from django.db import models
from django.contrib.auth.models import User

class Card(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField()

    def __str__(self):
        return self.word

class Correct(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='correct')
    last_correct = models.IntegerField(default=0)
    correct = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username}: {self.correct} correct answers"

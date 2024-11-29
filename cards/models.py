from django.db import models

class Card(models.Model):
    word = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    example = models.TextField()

    def __str__(self) -> str:
        return self.word

class Correct(models.Model):
    last_correct = models.CharField(max_length=100)
    correct = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.correct

class User(models.Model):
    login = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=20)
    correct = models.ForeignKey(Correct, on_delete=models.CASCADE, related_name='corrects')

    def __str__(self) -> str:
        return self.login

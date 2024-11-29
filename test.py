import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'language.config.settings')
django.setup()

from cards.models import Card

test_data = [
    {"word": "hello", "translation": "привет", "example": "Hello, how are you?"},
    {"word": "world", "translation": "мир", "example": "The world is beautiful."},
    {"word": "apple", "translation": "яблоко", "example": "I ate a red apple."},
    {"word": "book", "translation": "книга", "example": "I am reading a good book."},
    {"word": "cat", "translation": "кот", "example": "The cat is sleeping on the couch."},
]

for entry in test_data:
    Card.objects.create(
        word=entry["word"],
        translation=entry["translation"],
        example=entry["example"],
    )

print("для заполнения базы тестово")

'''
    "python test.py" для запуска
'''

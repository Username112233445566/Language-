from django.contrib import admin
from .models import Card, User, Correct

admin.site.register(Correct)
admin.site.register(User)
admin.site.register(Card)
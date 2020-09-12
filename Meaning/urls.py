from django.urls import path
from .views import search, save, show_words

app_name = 'Meanings'

urlpatterns = [
    path('search', search, name='search'),
    path('save', save, name='save'),
    path('words', show_words, name='words'),
]


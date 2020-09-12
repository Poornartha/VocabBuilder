from django.urls import path
from .views import home, result

app_name = 'practice'

urlpatterns = [
    path('', home, name='home'),
    path('result', result, name='result'),
]



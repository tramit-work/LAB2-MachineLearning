# lab2/urls.py
from django.urls import path
from .views import home, analyze_sentiment

urlpatterns = [
    path('', home, name='home'),
    path('analyze_sentiment/', analyze_sentiment, name='analyze_sentiment'),
]

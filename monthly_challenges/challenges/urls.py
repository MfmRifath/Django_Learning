from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path("", views.index),
    path('<int:month>', views.monthly_challenge_number),
    path('<str:month>', views.monthly_challenge, name='month-challenge'),
    
]
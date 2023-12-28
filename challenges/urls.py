from django.urls import path
from . import views

# this is a list python list
urlpatterns = [
    path('', views.index),
    path('<int:month>', views.monthy_challenge_by_number),
    path('<str:month>', views.monthy_challenge, name="month-challenge")
]

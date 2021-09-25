from os import name
from django.urls import path

from .views import ( RegistrationAPIView , LoginAPIView )

app_name = 'authentication'
urlpatterns = [
    path('user_registration/', RegistrationAPIView.as_view()),
    path('users/login/', LoginAPIView.as_view()),
]
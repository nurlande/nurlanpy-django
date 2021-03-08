from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets

from .serializers import RegistrationSerializer
from .serializers import UserSerializer
from .models import Registration
from .models import User


class RegistrationViewSet(viewsets.ModelViewSet):
    queryset = Registration.objects.all()
    serializer_class = RegistrationSerializer
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

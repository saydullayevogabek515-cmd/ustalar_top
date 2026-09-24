from django.shortcuts import render
from rest_framework.parsers import MultiPartParser, FormParser

from .models import Users
from .serializers import UsersSerializers
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    parser_classes = [MultiPartParser, FormParser]
    queryset = Users.objects.all()
    serializer_class = UsersSerializers
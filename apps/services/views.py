from django.shortcuts import render
from .models import Services
from .serializers import ServicesSerializer
from rest_framework import viewsets

class ServicesViewSet(viewsets.ModelViewSet):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
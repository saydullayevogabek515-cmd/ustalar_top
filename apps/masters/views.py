from django.shortcuts import render
from django_filters import rest_framework as django_filters
from rest_framework import filters
from rest_framework import viewsets
from .models import MasterProfile
from .serializers import MasterProfileSerializer
from .filter import MasterProfileFilter

class MasterProfileViewSet(viewsets.ModelViewSet):
    queryset = MasterProfile.objects.all()
    serializer_class = MasterProfileSerializer

    filter_backends = (django_filters.DjangoFilterBackend, filters.SearchFilter)
    filterset_class = MasterProfileFilter
    search_fields = ["category", 'name']
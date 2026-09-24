from django_filters import rest_framework as django_filters
from .models import MasterProfile

class MasterProfileFilter(django_filters.FilterSet):
    class Meta:
        model = MasterProfile
        fields = ['category', 'city', 'district']
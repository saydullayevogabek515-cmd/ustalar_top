from rest_framework import serializers
from .models import MasterProfile

class MasterProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MasterProfile
        fields = "__all__"
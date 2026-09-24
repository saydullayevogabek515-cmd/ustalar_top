from django.db import models
from apps.users.models import Users
from apps.categories.models import Category

class MasterProfile(models.Model):
    user = models.OneToOneField(Users, on_delete=models.CASCADE, related_name="master_profile")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="masters")
    bio = models.TextField(blank=True)
    experience_years = models.PositiveIntegerField(default=0)
    city = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    is_verified = models.BooleanField(default=False)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.firs_name
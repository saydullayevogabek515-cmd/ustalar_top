from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import RegexValidator

phone_regex = RegexValidator(
    regex=r'^\+998\d{9}$',
    message="Raqam +998xxxxxxxxx ko‘rinishida bo‘lishi kerak"
)

class Users(AbstractUser):
    ROLE_CHOICES = (
        ("CUSTOMER", "Customer"),
        ("MASTER", "Master"),
    )

    phone = models.CharField(
        validators=[phone_regex],
        unique=True,
        max_length=13
    )
    email = models.EmailField(unique=True, null=True, blank=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to="avatars/", null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default="CUSTOMER")

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
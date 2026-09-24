from django.db import models
from apps.masters.models import MasterProfile
from apps.categories.models import Category

class Services(models.Model):

    PRICE_TYPE = (
        ("FIXED", "Fixed"),
        ("FROM", "From"),
        ("NEGOTIABLE", "Negotiable")
    )

    master = models.ForeignKey(MasterProfile, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=12, decimal_places=0)
    duration = models.PositiveIntegerField()
    price_type = models.CharField(max_length=20, choices=PRICE_TYPE, default="FIXED")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.master and self.category
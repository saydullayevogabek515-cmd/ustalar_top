from django.db import models
from apps.users.models import Users
from apps.masters.models import MasterProfile
from apps.services.models import Services


class Order(models.Model):
    class Status(models.TextChoices):
        PENDING = "PENDING", "Pending"
        ACCEPTED = "ACCEPTED", "Accepted"
        REJECTED = "REJECTED", "Rejected"
        START = "START", "Start"
        IN_PROGRESS = "IN_PROGRESS", "In_progress"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    customer = models.ForeignKey(Users, on_delete=models.CASCADE)
    master = models.ForeignKey(MasterProfile, on_delete=models.CASCADE)
    services = models.ForeignKey(Services, on_delete=models.CASCADE)
    title = models.TextField()
    description = models.TextField()
    address = models.CharField(max_length=70, blank=True, null=False)
    city = models.CharField(max_length=70, blank=True, null=False)
    schedule_at = models.DateTimeField()
    price = models.DecimalField(max_digits=12, decimal_places=0)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.customer or self.master and self.title
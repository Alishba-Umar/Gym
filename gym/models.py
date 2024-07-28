from django.db import models
from django.utils import timezone
from datetime import timedelta

class Member(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Non Active', 'Non Active'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    fee_amount = models.DecimalField(max_digits=10, decimal_places=2)
    fee_date = models.DateField()
    picture = models.ImageField(upload_to='member_pictures/')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')

    def __str__(self):
        return self.name

    def is_due(self):
        next_due_date = self.fee_date + timedelta(days=30)
        return timezone.now().date() >= next_due_date - timedelta(days=2)

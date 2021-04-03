from django.db import models

# Create your models here.
class Payment(models.Model):
    recipient = models.CharField(max_length=50, null=False, blank=False)
    has_paid = models.BooleanField(null=False, blank=False, default=False)
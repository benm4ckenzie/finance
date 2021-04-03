from django.db import models

# Create your models here.


class Payment(models.Model):
    payment_category = models.CharField(max_length=50, null=False, blank=False)
    payment_account = models.CharField(max_length=50, null=False, blank=False, default="Starling (Joint)")
    payment_owner = models.CharField(max_length=50, null=False, blank=False, default="Household")
    payment_date = models.IntegerField(null=False, blank=False)
    instalment_amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    payment_recipient = models.CharField(max_length=50, null=False, blank=False)
    has_paid = models.BooleanField(null=False, blank=False, default=False)
    payment_completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.payment_recipient

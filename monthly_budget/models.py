from django.db import models

# Create your models here.

class Payment(models.Model):
    payment_category = models.CharField(max_length=50, null=False, blank=False)
    payment_account = models.CharField(max_length=50, null=False, blank=False, default="Starling (Joint)")
    payment_owner = models.CharField(max_length=50, null=False, blank=False)
    payment_date = models.IntegerField(null=False, blank=False)
    instalment_amount = models.DecimalField(max_digits=6, decimal_places=2, blank=False)
    payment_recipient = models.CharField(max_length=50, null=False, blank=False)
    has_paid = models.BooleanField(null=False, blank=False, default=False)
    payment_completion_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.payment_recipient


class Income(models.Model):
    income_stream = models.CharField(max_length=50, null=False, blank=False)
    income_amount = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False)
    has_recieved = models.BooleanField(null=False, blank=False, default=True)

    def __str__(self):
        return self.income_stream


class Balance(models.Model):
    joint_account_balance = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=True)
    #personal_account_balance = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=True)

    def __str__(self):
        return str(self.joint_account_balance)

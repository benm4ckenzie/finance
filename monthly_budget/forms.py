from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_category',
                'payment_account',
                'payment_owner',
                'payment_date',
                'instalment_amount',
                'payment_recipient',
                'payment_completion_date']
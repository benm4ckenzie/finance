from django import forms
from .models import Payment
from .models import Income


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_recipient', 'payment_category', 'payment_account', 'payment_owner', 'payment_date', 'payment_completion_date', 'instalment_amount']


class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_stream', 'income_amount']

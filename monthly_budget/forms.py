from django import forms
from .models import Payment, Income, Balance

class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['payment_category',
                'payment_account',
                'payment_owner',
                'payment_date',
                'instalment_amount',
                'payment_recipient',
                'payment_completion_date',
                'has_paid']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_stream',
                'income_amount',
                'has_recieved']

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['joint_account_balance',
                'personal_account_balance']
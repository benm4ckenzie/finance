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
        widgets = {
            'payment_category': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_account': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_owner': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_date': forms.TextInput(attrs={'class': 'form-control'}),
            'instalment_amount': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_recipient': forms.TextInput(attrs={'class': 'form-control'}),
            'payment_completion_date': forms.DateInput(attrs={'class': 'form-control'})
        }

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['income_stream',
                  'income_amount',
                  'has_recieved']
        widgets = {
            'income_stream': forms.TextInput(attrs={'class': 'form-control'}),
            'income_amount': forms.TextInput(attrs={'class': 'form-control'})
        }

class BalanceForm(forms.ModelForm):
    class Meta:
        model = Balance
        fields = ['joint_account_balance',
                  'personal_account_balance']
        widgets = {
            'joint_account_balance': forms.TextInput(attrs={'class': 'form-control'}),
            'personal_account_balance': forms.TextInput(attrs={'class': 'form-control'})
        }

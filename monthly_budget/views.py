from django.shortcuts import render
from .models import Payment
from .models import Income

# Create your views here.


def get_monthly_budget_list(request):
    payments = Payment.objects.all()
    incomes = Income.objects.all()
    context = {
        'payments' : payments,
        'incomes' : incomes
    }
    return render(request, 'monthly_budget/monthly_budget_list.html', context)


def add_payment(request):
    return render(request, 'monthly_budget/add_payment.html')


def add_income(request):
    return render(request, 'monthly_budget/add_income.html')

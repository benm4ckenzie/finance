from django.shortcuts import render, redirect
from .models import Payment
from .models import Income
from .forms import PaymentForm
from .forms import IncomeForm

# Create your views here.


def get_monthly_budget_list(request):
    payments = Payment.objects.all()
    incomes = Income.objects.all()
    context = {
        'payments': payments,
        'incomes': incomes
    }
    return render(request, 'monthly_budget/monthly_budget_list.html', context)


def add_payment(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('get_monthly_budget_list')
    form = PaymentForm()
    context = {
        'form': form
    }

    return render(request, 'monthly_budget/add_payment.html', context)


def add_income(request):
    if request.method == 'POST':
        incomeForm = IncomeForm(request.POST)
        if incomeForm.is_valid():
            incomeForm.save()
            return redirect('get_monthly_budget_list')
    incomeForm = IncomeForm()
    context = {
        'incomeForm': incomeForm
    }

    return render(request, 'monthly_budget/add_income.html', context)

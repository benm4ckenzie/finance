from django.shortcuts import render, redirect, get_object_or_404
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
        paymentForm = PaymentForm(request.POST)
        if paymentForm.is_valid():
            paymentForm.save()
            return redirect('get_monthly_budget_list')
    paymentForm = PaymentForm()
    context = {
        'paymentForm': paymentForm
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


def edit_payment(request, payment_id):
    paymentItem = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        paymentForm = PaymentForm(request.POST, instance=paymentItem)
        if paymentForm.is_valid():
            paymentForm.save()
            return redirect('get_monthly_budget_list')
    editPaymentForm = PaymentForm(instance=paymentItem)
    context ={
        'editPaymentForm': editPaymentForm
    }
    return render(request, 'monthly_budget/edit_payment.html', context)
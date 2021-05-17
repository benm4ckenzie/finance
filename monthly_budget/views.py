from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import Payment
from .models import Income
from .forms import PaymentForm
from .forms import IncomeForm

# Create your views here.


def get_monthly_budget_list(request):
    payments = Payment.objects.all()
    income = Income.objects.all()
    sumOfPayments = payments.aggregate(Sum('instalment_amount'))['instalment_amount__sum']
    sumOfIncome = income.aggregate(Sum('income_amount'))['income_amount__sum']
    incomePaymentsDifference = sumOfIncome - sumOfPayments
    context = {
        'payments': payments,
        'sumOfPayments': sumOfPayments,
        'sumOfIncome': sumOfIncome,
        'incomePaymentsDifference': incomePaymentsDifference
    }
    return render(request, 'monthly_budget/monthly_budget_list.html', context)


def get_monthly_income_list(request):
    incomes = Income.objects.all()
    context = {
        'incomes': incomes
    }
    return render(request, 'monthly_budget/monthly_income_list.html', context)


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


def edit_payment(request, payment_id):
    paymentItem = get_object_or_404(Payment, id=payment_id)
    if request.method == 'POST':
        paymentForm = PaymentForm(request.POST, instance=paymentItem)
        if paymentForm.is_valid():
            paymentForm.save()
            return redirect('get_monthly_budget_list')
    editPaymentForm = PaymentForm(instance=paymentItem)
    context = {
        'editPaymentForm': editPaymentForm
    }
    return render(request, 'monthly_budget/edit_payment.html', context)


def has_paid(request, payment_id):
    paymentItem = get_object_or_404(Payment, id=payment_id)
    paymentItem.has_paid = not paymentItem.has_paid
    paymentItem.save()
    return redirect('get_monthly_budget_list')


def delete_payment(request, payment_id):
    paymentItem = get_object_or_404(Payment, id=payment_id)
    paymentItem.delete()
    return redirect('get_monthly_budget_list')


def add_income(request):
    if request.method == 'POST':
        incomeForm = IncomeForm(request.POST)
        if incomeForm.is_valid():
            incomeForm.save()
            return redirect('get_monthly_income_list')
    incomeForm = IncomeForm()
    context = {
        'incomeForm': incomeForm
    }
    return render(request, 'monthly_budget/add_income.html', context)


def edit_income(request, income_id):
    incomeItem = get_object_or_404(Income, id=income_id)
    if request.method == 'POST':
        incomeForm = IncomeForm(request.POST, instance=incomeItem)
        if incomeForm.is_valid():
            incomeForm.save()
            return redirect('get_monthly_income_list')
    editIncomeForm = IncomeForm(instance=incomeItem)
    context = {
        'editIncomeForm': editIncomeForm
    }
    return render(request, 'monthly_budget/edit_income.html', context)


def has_recieved(request, income_id):
    incomeItem = get_object_or_404(Income, id=income_id)
    incomeItem.has_recieved = not incomeItem.has_recieved
    incomeItem.save()
    return redirect('get_monthly_income_list')


def delete_income(request, income_id):
    incomeItem = get_object_or_404(Income, id=income_id)
    incomeItem.delete()
    return redirect('get_monthly_income_list')

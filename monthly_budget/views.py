from django.shortcuts import render, redirect
from .models import Payment
from .models import Income
from .forms import PaymentForm

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
        payment_category = request.POST.get('payment_category')
        payment_account = request.POST.get('payment_account')
        payment_owner = request.POST.get('payment_owner')
        payment_date = request.POST.get('payment_date')
        payment_recipient = request.POST.get('recipient_name')
        payment_completion_date = request.POST.get('payment_completion_date')
        instalment_amount = request.POST.get('instalmetn_amount')
        Payment.object.create(payment_category=payment_category,
            payment_account=payment_account,
            payment_owner=payment_owner,
            payment_date=payment_date,
            payment_recipient=payment_recipient,
            payment_completion_date=payment_completion_date,
            instalment_amount=instalment_amount)

        return redirect('get_monthly_budget_list')
            form = PaymentForm()
        context = {
            'form': form
}
    return render(request, 'monthly_budget/add_payment.html', context)


def add_income(request):
    if request.method == 'POST':
        income_stream = request.POST.get('income_stream')
        income_amount = request.POST.get('income_amount')
        Income.object.create(income_stream=income_stream, income_amount=income_amount)

        return redirect('get_monthly_budget_list')

    return render(request, 'monthly_budget/add_income.html')

from django.shortcuts import render

# Create your views here.

def get_monthly_budget_list(request):
    return render(request, 'monthly_budget/monthly_budget_list.html')

"""finance URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from monthly_budget import views

urlpatterns = [
    path('admin', admin.site.urls),
    path('', views.home_page, name='home_page'),
    path('monthly_budget_list', views.get_monthly_budget_list, name='get_monthly_budget_list'),
    path('payment', views.add_payment, name='payment'),
    path('edit_payment/<payment_id>', views.edit_payment, name='edit_payment'),
    path('has_paid/<payment_id>', views.has_paid, name='has_paid'),
    path('delete_payment/<payment_id>', views.delete_payment, name='delete_payment'),
    path('monthly_income_list', views.get_monthly_income_list, name='get_monthly_income_list'),
    path('income', views.add_income, name='income'),
    path('edit_income/<income_id>', views.edit_income, name='edit_income'),
    path('has_recieved/<income_id>', views.has_recieved, name='has_recieved'),
    path('delete_income/<income_id>', views.delete_income, name='delete_income'),
    path('balance', views.add_balance, name='balance'),
    path('edit_balance/<balance_id>', views.edit_balance, name='edit_balance'),
    url('accounts/', include('allauth.urls')),
]

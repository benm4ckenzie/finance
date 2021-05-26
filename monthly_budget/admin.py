from django.contrib import admin
from .models import Payment, Income, Balance

# Register your models here.
admin.site.register(Payment)
admin.site.register(Income)
admin.site.register(Balance)

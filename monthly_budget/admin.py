from django.contrib import admin
from .models import Payment
from .models import Income

# Register your models here.
admin.site.register(Payment)
admin.site.register(Income)

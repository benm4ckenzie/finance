# Generated by Django 3.2.6 on 2021-08-27 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_budget', '0003_remove_payment_payment_note'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='balance',
            name='personal_account_balance',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='payment_account',
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_owner',
            field=models.CharField(max_length=50),
        ),
    ]

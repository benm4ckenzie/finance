# Generated by Django 3.2.6 on 2021-08-27 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monthly_budget', '0004_auto_20210827_1049'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='payment_account',
            field=models.CharField(default='Starling (Joint)', max_length=50),
        ),
    ]

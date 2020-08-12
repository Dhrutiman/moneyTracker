# Generated by Django 3.0.8 on 2020-08-11 13:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_bank_csv', '0008_auto_20200811_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(blank=True, choices=[('Travels', 'TRAVELS'), ('Food', 'FOOD'), ('Donation', 'DONATION'), ('Grocery', 'GROCERY'), ('MonthlyRent', 'MONTHLY RENT'), ('Shopping', 'SHOPPING'), ('UtilityBills', 'UTILITY BITTS'), ('Call&Internet', 'CALL AND INTERNET'), ('Entertanment', 'ENTERTANMENT'), ('Clothing', 'CLOTHING'), ('Loan', 'LOAN OR HELP'), ('Others', 'OTHERS'), ('Investment', 'INVESTMENT'), ('Education', 'EDUCATION')], default='OTHERS', max_length=30, null=True),
        ),
    ]

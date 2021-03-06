# Generated by Django 3.0.8 on 2020-08-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_bank_csv', '0010_auto_20200811_1844'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(blank=True, choices=[('Travels', 'TRAVELS'), ('Food', 'FOOD'), ('Donation', 'DONATION'), ('Grocery', 'GROCERY'), ('MonthlyRent', 'MONTHLY RENT'), ('Shopping', 'SHOPPING'), ('UtilityBills', 'UTILITY BITTS'), ('Call&Internet', 'CALL AND INTERNET'), ('Entertanment', 'ENTERTANMENT'), ('Clothing', 'CLOTHING'), ('Loan', 'LOAN OR HELP'), ('Others', 'OTHERS'), ('Investment', 'INVESTMENT'), ('Education', 'EDUCATION'), ('None', 'NONE')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='sbject',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]

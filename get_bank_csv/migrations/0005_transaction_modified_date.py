# Generated by Django 3.0.8 on 2020-08-11 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('get_bank_csv', '0004_auto_20200811_0921'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='modified_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
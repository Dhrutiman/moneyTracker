# Generated by Django 3.0.8 on 2020-08-14 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('get_bank_csv', '0018_auto_20200814_1342'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ('-id',)},
        ),
    ]

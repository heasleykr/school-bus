# Generated by Django 4.1.1 on 2023-01-18 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='account_type',
            field=models.CharField(choices=[(1, 'Checking'), ('2', 'Savings')], max_length=36),
        ),
    ]

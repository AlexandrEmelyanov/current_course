# Generated by Django 5.0.1 on 2024-01-25 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('course', models.FloatField(verbose_name='Course')),
                ('last_update', models.DateTimeField(verbose_name='Last update')),
            ],
            options={
                'verbose_name': 'Currency rate',
                'verbose_name_plural': 'Currency rates',
            },
        ),
    ]

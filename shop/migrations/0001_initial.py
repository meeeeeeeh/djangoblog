# Generated by Django 3.1.3 on 2020-11-30 17:08

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, verbose_name='Название')),
                ('description', models.TextField(max_length=200, verbose_name='Описание')),
                ('cost', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0.00'), max_digits=10, null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товары',
            },
        ),
    ]

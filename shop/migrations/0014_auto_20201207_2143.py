# Generated by Django 3.1.3 on 2020-12-07 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.TextField(choices=[('Обработка заказа', 'Обработка заказа'), ('Доставка', 'Доставка'), ('Получен', 'Получен')], max_length=30),
        ),
    ]

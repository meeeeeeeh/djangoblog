# Generated by Django 3.1.3 on 2020-11-25 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0021_auto_20201125_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, default=None, upload_to='images/'),
        ),
    ]

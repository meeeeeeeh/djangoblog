# Generated by Django 3.1.3 on 2020-11-21 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0, verbose_name='Просмотры'),
        ),
    ]

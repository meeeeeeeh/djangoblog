# Generated by Django 3.1.3 on 2020-11-22 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_auto_20201122_1544'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='dislike',
        ),
        migrations.RemoveField(
            model_name='post',
            name='like',
        ),
        migrations.AddField(
            model_name='post',
            name='dislikes',
            field=models.IntegerField(default=0, verbose_name='Дизлайки'),
        ),
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0, verbose_name='Лайки'),
        ),
    ]
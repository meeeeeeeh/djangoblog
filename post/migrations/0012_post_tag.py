# Generated by Django 3.1.3 on 2020-11-23 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0011_remove_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='post.tag', verbose_name='Теги'),
            preserve_default=False,
        ),
    ]

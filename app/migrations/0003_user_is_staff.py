# Generated by Django 2.2.5 on 2020-07-06 22:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200707_0059'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=True, verbose_name='staff'),
        ),
    ]

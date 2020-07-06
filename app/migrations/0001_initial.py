# Generated by Django 2.2.5 on 2020-07-05 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='media')),
                ('name', models.CharField(max_length=125)),
                ('price', models.FloatField()),
            ],
        ),
    ]

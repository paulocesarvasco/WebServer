# Generated by Django 3.2.3 on 2021-07-17 01:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('server', '0002_auto_20210717_0051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagemodel',
            name='expirationDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='messagemodel',
            name='startDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
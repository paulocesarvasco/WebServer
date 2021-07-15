# Generated by Django 3.2.5 on 2021-07-15 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('startDate', models.DateTimeField()),
                ('expirationDate', models.DateTimeField()),
            ],
        ),
    ]

# Generated by Django 3.2 on 2021-05-13 14:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deposit', models.CharField(max_length=50)),
                ('term', models.CharField(max_length=50)),
                ('rate', models.CharField(max_length=50)),
                ('interest', models.CharField(max_length=50)),
            ],
        ),
    ]

# Generated by Django 3.1 on 2023-10-20 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20231020_1410'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='last_login',
            field=models.DateField(auto_now=True),
        ),
    ]

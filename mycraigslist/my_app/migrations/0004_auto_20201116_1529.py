# Generated by Django 3.1 on 2020-11-16 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0003_auto_20201115_0318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='search',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
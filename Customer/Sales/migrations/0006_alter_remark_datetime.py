# Generated by Django 4.2.2 on 2023-06-08 09:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sales', '0005_alter_customer_nature_of_business_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remark',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]

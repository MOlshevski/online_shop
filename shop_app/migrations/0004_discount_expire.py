# Generated by Django 4.1.1 on 2022-10-21 16:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0003_alter_basket_number_of_items'),
    ]

    operations = [
        migrations.AddField(
            model_name='discount',
            name='expire',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
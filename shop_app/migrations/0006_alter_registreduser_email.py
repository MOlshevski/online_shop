# Generated by Django 4.1.1 on 2022-10-26 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0005_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registreduser',
            name='email',
            field=models.EmailField(default=None, max_length=254),
        ),
    ]

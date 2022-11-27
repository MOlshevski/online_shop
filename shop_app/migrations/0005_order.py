# Generated by Django 4.1.1 on 2022-10-21 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop_app', '0004_discount_expire'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_date', models.DateTimeField()),
                ('result_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('product_items', models.JSONField()),
                ('delivery_address', models.CharField(max_length=500)),
                ('delivery_date', models.DateTimeField()),
                ('delivery_method', models.CharField(choices=[('Courier', 'Courier'), ('Pickup', 'Pickup'), ('Post', 'Post')], max_length=10)),
                ('delivery_status', models.CharField(choices=[('Delivered', 'Delivered'), ('In Process', 'In Process')], max_length=10)),
                ('payment_method', models.CharField(choices=[('Cash', 'Cash'), ('Card', 'Card')], max_length=10)),
                ('payment_status', models.CharField(choices=[('Paid', 'Paid'), ('Waiting', 'Waiting')], max_length=10)),
                ('delivery_notif_required', models.BooleanField(default=True)),
                ('delivery_notif_in_time', models.IntegerField(choices=[(1, 1), (6, 6), (24, 24)], default=1)),
                ('delivery_notif_sent', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

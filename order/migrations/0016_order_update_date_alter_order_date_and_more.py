# Generated by Django 4.1 on 2022-12-03 10:24

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0015_remove_orderdata_forw_ip_alter_order_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='update_date',
            field=models.DateField(default=datetime.datetime(2022, 12, 3, 10, 24, 21, 932849, tzinfo=datetime.timezone.utc), verbose_name='Update Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 10, 24, 21, 932849, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 3, 10, 24, 21, 932849, tzinfo=datetime.timezone.utc), verbose_name='Date'),
        ),
    ]

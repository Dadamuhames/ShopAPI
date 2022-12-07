# Generated by Django 4.1 on 2022-12-01 12:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0011_alter_order_date_alter_orderhistory_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='comment',
            field=models.TextField(default='some comment', verbose_name='Comment'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='email',
            field=models.EmailField(default='dadamuhames@gmail.com', max_length=254, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='order',
            name='post_ind',
            field=models.CharField(default='POS-23', max_length=6, verbose_name='Post Index'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 17, 6, 29, 335826), verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='orderhistory',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 1, 17, 6, 29, 336836), verbose_name='Date'),
        ),
    ]

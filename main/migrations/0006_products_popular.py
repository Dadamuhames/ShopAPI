# Generated by Django 4.1 on 2022-11-24 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_products_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='popular',
            field=models.BooleanField(default=False, verbose_name='Popular'),
        ),
    ]

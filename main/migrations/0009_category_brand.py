# Generated by Django 4.1 on 2022-11-24 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_remove_products_popular_productvariants_popular'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='brand',
            field=models.BooleanField(default=False, verbose_name='Is Brand'),
        ),
    ]

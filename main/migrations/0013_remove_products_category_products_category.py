# Generated by Django 4.1 on 2022-11-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_remove_products_rating_productvariants_rating_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='category',
        ),
        migrations.AddField(
            model_name='products',
            name='category',
            field=models.ManyToManyField(related_name='products', to='main.category'),
        ),
    ]

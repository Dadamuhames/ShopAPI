# Generated by Django 4.1 on 2022-11-25 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_rename_atibuts_atributs'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='colors',
            field=models.ManyToManyField(blank=True, null=True, to='main.color'),
        ),
    ]

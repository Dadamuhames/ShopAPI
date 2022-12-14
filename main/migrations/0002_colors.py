# Generated by Django 4.1 on 2022-11-24 11:39

import colorfield.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Colors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True, verbose_name='Color name')),
                ('hex', colorfield.fields.ColorField(default='#FF0000', image_field=None, max_length=18, samples=None)),
            ],
        ),
    ]

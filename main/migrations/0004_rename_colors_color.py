# Generated by Django 4.1 on 2022-11-24 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_productvariants_color'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Colors',
            new_name='Color',
        ),
    ]

# Generated by Django 4.1 on 2022-11-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0002_state_city_order_city_alter_order_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Performed', 'Performed'), ('Canseled', 'Canseled'), ('Paid', 'Paid')], default='Accepted', max_length=255, verbose_name='Status'),
        ),
    ]

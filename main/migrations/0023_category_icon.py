# Generated by Django 4.1 on 2022-12-04 16:44

from django.db import migrations
import easy_thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_products_prod_of_day_alter_products_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='icon',
            field=easy_thumbnails.fields.ThumbnailerImageField(blank=True, null=True, upload_to='category_icons'),
        ),
    ]

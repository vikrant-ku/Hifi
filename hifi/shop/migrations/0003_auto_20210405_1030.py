# Generated by Django 3.1.7 on 2021-04-05 05:00

import datetime
from django.db import migrations
from django.utils.timezone import utc
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_sub_category_type_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_color',
            name='image1',
            field=django_resized.forms.ResizedImageField(crop=['middle', 'center'], default=datetime.datetime(2021, 4, 5, 5, 0, 17, 234578, tzinfo=utc), force_format=None, keep_meta=True, quality=75, size=[700, 900], upload_to='media/product/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product_color',
            name='image2',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=75, size=[700, 900], upload_to='media/product/'),
        ),
        migrations.AddField(
            model_name='product_color',
            name='image3',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=75, size=[700, 900], upload_to='media/product/'),
        ),
        migrations.AddField(
            model_name='product_color',
            name='image4',
            field=django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=75, size=[700, 900], upload_to='media/product/'),
        ),
    ]
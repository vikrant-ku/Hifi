# Generated by Django 3.1.7 on 2021-04-13 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0011_auto_20210413_1612'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='alt_mobile',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
    ]

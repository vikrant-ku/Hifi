# Generated by Django 3.1.7 on 2021-04-13 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_auto_20210410_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='billing',
            name='pin',
            field=models.CharField(default='', max_length=6),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-14 04:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20210413_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact_us',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
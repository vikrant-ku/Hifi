# Generated by Django 3.1.7 on 2021-04-10 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_billing'),
    ]

    operations = [
        migrations.RenameField(
            model_name='billing',
            old_name='date',
            new_name='created',
        ),
    ]
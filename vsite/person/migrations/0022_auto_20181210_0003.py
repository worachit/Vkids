# Generated by Django 2.1.3 on 2018-12-09 17:03

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0021_admin_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, unique=True),
        ),
    ]
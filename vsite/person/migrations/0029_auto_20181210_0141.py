# Generated by Django 2.1.3 on 2018-12-09 18:41

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0028_auto_20181210_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='school',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.School'),
        ),
        migrations.AlterField(
            model_name='parent',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='parent',
            name='student',
            field=models.ManyToManyField(blank=True, to='person.Student'),
        ),
    ]

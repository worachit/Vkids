# Generated by Django 2.1.3 on 2018-12-09 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0013_auto_20181209_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.CharField(blank=True, choices=[('NORMAL', 'ปกติ'), ('INBUS', 'อยู่ในรถ'), ('OUTBUS', 'ลงรถ'), ('PROBLM', 'ผิดปกติ')], default='NORMAL', max_length=6),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-09 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20181209_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bus',
            name='active',
        ),
        migrations.RemoveField(
            model_name='bus',
            name='description',
        ),
        migrations.AddField(
            model_name='bus',
            name='status',
            field=models.CharField(choices=[('NORM', 'ปกติ'), ('PROB', 'ผิดปกติ'), ('ACCI', 'เกิดอุบัติเหตุ')], default='NORM', max_length=4),
        ),
    ]

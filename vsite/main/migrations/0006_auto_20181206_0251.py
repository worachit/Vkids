# Generated by Django 2.1.3 on 2018-12-05 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_history_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='avg_speed',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='bus',
            name='max_speed',
            field=models.IntegerField(default=0),
        ),
    ]

# Generated by Django 2.1.3 on 2018-12-07 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0005_auto_20181207_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='test',
            field=models.CharField(default='test', max_length=10),
        ),
    ]

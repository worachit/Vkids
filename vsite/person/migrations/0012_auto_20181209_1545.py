# Generated by Django 2.1.3 on 2018-12-09 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0011_student_school'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='bag_weight',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='student',
            name='status',
            field=models.CharField(choices=[('NORM', 'ปกติ'), ('PROB', 'ผิดปกติ')], default='NORM', max_length=4),
        ),
    ]

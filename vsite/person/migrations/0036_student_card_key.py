# Generated by Django 2.1.3 on 2018-12-16 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0035_remove_student_scan_count'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='card_key',
            field=models.CharField(max_length=15, null=True),
        ),
    ]

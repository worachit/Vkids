# Generated by Django 2.1.3 on 2018-12-16 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0036_student_card_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='bag_weight',
        ),
    ]
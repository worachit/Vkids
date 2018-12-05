# Generated by Django 2.1.3 on 2018-12-05 19:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0002_admin_parent'),
        ('main', '0003_history_student'),
    ]

    operations = [
        migrations.AddField(
            model_name='history',
            name='driver',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Driver'),
        ),
        migrations.AddField(
            model_name='history',
            name='teacher',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='person.Teacher'),
        ),
    ]

# Generated by Django 3.2.4 on 2021-08-05 16:44

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('aidApp', '0014_patient_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='age',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='app_date',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 16, 44, 46, 831048, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='patient',
            name='D_O_B',
            field=models.DateField(default=datetime.datetime(2021, 8, 5, 16, 44, 46, 829048, tzinfo=utc)),
        ),
    ]
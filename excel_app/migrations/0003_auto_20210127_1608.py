# Generated by Django 3.1.5 on 2021-01-27 12:08

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel_app', '0002_contact_create_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 27, 16, 8, 13, 251636)),
        ),
    ]
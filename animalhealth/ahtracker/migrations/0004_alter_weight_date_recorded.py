# Generated by Django 3.2.3 on 2021-06-13 21:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ahtracker', '0003_alter_weight_date_recorded'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight',
            name='date_recorded',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 7, 41, 35, 277936), verbose_name='date recorded'),
        ),
    ]

# Generated by Django 3.2.3 on 2021-06-13 22:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ahtracker', '0006_alter_weight_date_recorded'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sex', models.CharField(max_length=25)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='weight',
            name='date_recorded',
            field=models.DateTimeField(default=datetime.datetime(2021, 6, 14, 8, 53, 12, 391847), verbose_name='date recorded'),
        ),
        migrations.AlterField(
            model_name='animal',
            name='sex',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ahtracker.sex'),
        ),
    ]

# Generated by Django 3.2.8 on 2021-12-10 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_remove_route_shedule_delay_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route_shedule',
            name='arrival_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='route_shedule',
            name='departure_date',
            field=models.DateField(),
        ),
    ]

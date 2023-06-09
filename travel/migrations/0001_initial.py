# Generated by Django 3.2.8 on 2021-12-09 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route_shedule',
            fields=[
                ('serial_number', models.AutoField(primary_key=True, serialize=False)),
                ('route_number', models.CharField(max_length=100)),
                ('flight_number', models.CharField(max_length=100)),
                ('airline_name', models.CharField(max_length=100)),
                ('flight', models.CharField(max_length=100)),
                ('departure_airport', models.CharField(max_length=100)),
                ('arrival_airport', models.CharField(max_length=100)),
                ('departure_time', models.DateTimeField()),
                ('arrival_time', models.DateTimeField()),
                ('flight_status', models.CharField(max_length=100)),
                ('delay_time', models.DateField()),
            ],
        ),
    ]

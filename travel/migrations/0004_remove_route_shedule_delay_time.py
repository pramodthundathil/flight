# Generated by Django 3.2.8 on 2021-12-10 02:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0003_auto_20211210_0225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='route_shedule',
            name='delay_time',
        ),
    ]

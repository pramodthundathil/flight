# Generated by Django 3.2.14 on 2023-04-18 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('travel', '0008_alter_bookings_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bookings',
            old_name='numpass',
            new_name='number_of_passengers',
        ),
        migrations.RenameField(
            model_name='bookings',
            old_name='passportnumber',
            new_name='passport_number',
        ),
        migrations.AlterField(
            model_name='bookings',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]

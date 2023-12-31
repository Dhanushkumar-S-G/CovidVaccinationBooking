# Generated by Django 3.2.19 on 2023-06-23 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0005_appointment_dose_booked_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='appointment_status',
            field=models.IntegerField(choices=[(1, 'BOOKED'), (2, 'VACCINATED'), (3, 'CANCELED'), (4, 'EXPIRED')], default=1),
        ),
    ]

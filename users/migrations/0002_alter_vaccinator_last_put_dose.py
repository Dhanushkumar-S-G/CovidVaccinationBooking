# Generated by Django 3.2.19 on 2023-06-23 10:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('admindashboard', '0005_appointment_dose_booked_for'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccinator',
            name='last_put_dose',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='related_vaccinators', to='admindashboard.dose'),
        ),
    ]

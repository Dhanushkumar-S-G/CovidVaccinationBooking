# Generated by Django 3.2.19 on 2023-06-21 17:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('admindashboard', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vaccinator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('aadhar_number', models.PositiveBigIntegerField(unique=True)),
                ('dob', models.DateField()),
                ('mobile_number', models.BigIntegerField()),
                ('gender', models.IntegerField(choices=[(1, 'MALE'), (2, 'FEMALE'), (3, 'OTHERS')])),
                ('last_put_dose', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='related_vaccinators', to='admindashboard.dose')),
            ],
        ),
    ]

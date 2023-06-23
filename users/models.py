from django.db import models
from django.contrib.auth.models import User


class Vaccinator(models.Model):
    
    MALE = 1
    FEMALE = 2
    OTHERS = 3

    GENDER_CHOICES   = (
        (MALE,'MALE'),
        (FEMALE,'FEMALE'),
        (OTHERS,'OTHERS')
    )


    name = models.CharField(max_length=50)
    aadhar_number = models.PositiveBigIntegerField(unique=True)
    dob = models.DateField()
    mobile_number  = models.BigIntegerField()
    last_put_dose = models.ForeignKey('admindashboard.Dose',related_name='related_vaccinators',on_delete=models.PROTECT,null=True,blank=True)
    gender = models.IntegerField(choices=GENDER_CHOICES)
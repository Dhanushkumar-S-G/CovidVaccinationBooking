from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from users.models import Vaccinator




class Medicine(models.Model):
    name = models.CharField(max_length=50)
    made_by = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class Location(models.Model):
    name = models.CharField(max_length=50)
    pincode = models.CharField(max_length=6)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    regular_available_medicines = models.ManyToManyField(Medicine)

    def __str__(self) -> str:
        return f'{self.name} - {self.pincode}' 
     

class Slot(models.Model):
    name = models.CharField(max_length=50,null=True,blank=True)
    location = models.ForeignKey(Location,related_name='related_slots',on_delete=models.CASCADE,null=True)
    from_time = models.TimeField()
    to_time = models.TimeField()

    def __str__(self) -> str:
        return f'{self.name} - {self.from_time} to {self.to_time}'
        

class Dose(models.Model):
    name = models.CharField(max_length=10)
    prev = models.ForeignKey('self',related_name='next',on_delete=models.SET_NULL,null=True,blank=True)


class Appointment(models.Model):

    BOOKED = 1
    VACCINATED = 2
    CANCELED = 3

    APPOINTMENT_STATUS_CHOICES = (
        (BOOKED,'BOOKED'),
        (VACCINATED,'VACCINATED'),
        (CANCELED, 'CANCELED')  
    )

    booked_by = models.ForeignKey(User,on_delete=models.PROTECT,related_name='related_bookings')
    booked_for = models.ForeignKey(Vaccinator,on_delete=models.PROTECT,related_name='related_appointments')
    booked_at = models.DateTimeField(auto_now_add=True)
    appointment_date = models.DateField()
    booked_slot = models.ForeignKey(Slot,on_delete=models.SET_NULL,null=True)
    appointment_status = models.IntegerField(choices=APPOINTMENT_STATUS_CHOICES,default=1)
    location = models.ForeignKey(Location,on_delete=models.CASCADE,related_name='related_appointments')

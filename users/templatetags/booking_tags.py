from django import template
from users.models import Vaccinator
from admindashboard.models import Appointment
from django.db.models import Q
from datetime import datetime


register = template.Library()

@register.simple_tag()
def get_active_bookings(id):
    vaccinator = Vaccinator.objects.get(id=id)
    if Appointment.objects.filter(Q(booked_for = vaccinator) & Q(appointment_status=Appointment.BOOKED) &Q(booked_at__gte = datetime.now().date())).exists():
        apppointments = Appointment.objects.filter(Q(booked_for = vaccinator) & Q(appointment_status=Appointment.BOOKED)).first()
        return apppointments.appointment_date
    else:
        return None
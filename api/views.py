from admindashboard.models import Location,Slot,Appointment
from users.models import Vaccinator
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,SAFE_METHODS
from django.db.models import Q,Count
from datetime import datetime,timedelta


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_locations(request,pincode):

    if len(pincode) < 6:
        return JsonResponse(status=403,data={'error':'invalid pincode'})
    
    if Location.objects.filter(pincode = pincode).exists():
        locations = Location.objects.filter(pincode=pincode)
        serialized_data = FindLocationSerializer(locations,many=True).data
        return JsonResponse({'locations':serialized_data})
    else:
        return JsonResponse(status=200,data={'success':'no active centers found'})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])    
def get_slots(request,id,date):
    try:
        location = Location.objects.get(id=id)
    except Exception as e:
        return JsonResponse(status=403,data={'error':'not a valid location'})
    
    date = datetime.strptime(date,"%d-%m-%Y").date()

    if location.related_slots.exists():
        slots = location.related_slots
        booked_appointments = Appointment.objects.filter(appointment_date=date).exclude(appointment_status=Appointment.CANCELED)
        booked_slots = [x.booked_slot.id for x in booked_appointments]
        print(booked_slots)
        slots = slots.exclude(id__in = booked_slots)
        serialized_data = LocationSlotSerializer(slots,many=True).data
        return JsonResponse(status=200,data={'slots':serialized_data})

    else:
        return JsonResponse(status=200,data={'success':'No active slots found'})
    

@api_view(['GET'])
@permission_classes([IsAuthenticated])    
def get_dose(request,aadhar):

    if Vaccinator.objects.filter(aadhar_number=aadhar).exists():
        vaccinator = Vaccinator.objects.filter(aadhar_number = aadhar).first()
        last_dose = vaccinator.last_put_dose
        if not last_dose:
            dose = Dose.objects.filter(prev__isnull=True).first()
            serialized_data = DoseSerializer(dose).data
        elif last_dose.next.first() == None:
            return JsonResponse(status=200,data={'success':'Vaccinator took all doses'})
        else:
            
            dose = last_dose.next.first()
            serialized_data = DoseSerializer(dose).data

    else:
        dose = Dose.objects.filter(prev__isnull=True).first()
        serialized_data = DoseSerializer(dose).data

    return JsonResponse(status=200,data={'dose':serialized_data})



@api_view(['GET'])
@permission_classes([IsAuthenticated])  
def get_available_dates(request,id):
    from_date = datetime.now().date()
    to_date = from_date + timedelta(days=10)
    total_appointments = Appointment.objects.filter(Q(location__id = id) & Q(appointment_date__gte=from_date) & Q(appointment_date__lte=to_date)).exclude(appointment_status=3)
    appointments = []
    for i in range(10):
        current_date = from_date + timedelta(days=i)
        appointments_left = 10 - total_appointments.filter(appointment_date = current_date).count()
        appointments.append([current_date.strftime("%d-%m-%Y"),appointments_left])

    return JsonResponse({'appointments': appointments})


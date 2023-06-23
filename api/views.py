from admindashboard.models import Location,Slot
from users.models import Vaccinator
from django.http import JsonResponse
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated,SAFE_METHODS


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
def get_slots(request,id):
    try:
        location = Location.objects.get(id=id)
    except Exception as e:
        return JsonResponse(status=403,data={'error':'not a valid location'})
    if location.related_slots.exists():
        slots = location.related_slots
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

        if last_dose.next == None:
            return JsonResponse(status=200,data={'success':'Vaccinator took all doses'})
        else:
            dose = last_dose.next
            serialized_data = DoseSerializer(dose).data

    else:
        dose = Dose.objects.filter(prev__isnull=True).first()
        serialized_data = DoseSerializer(dose).data

    return JsonResponse(status=200,data={'doses':serialized_data})

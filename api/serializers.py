from rest_framework import serializers
from admindashboard.models import Location,Slot,Dose,Medicine


class FindLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class LocationSlotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Slot
        exclude = ('location',)


class DoseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dose
        fields = ['name']


class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = ['name','id']
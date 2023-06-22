from django.forms import ModelForm
from .models import *
from django import forms


class SlotForm(ModelForm):
    name = forms.CharField(max_length=50,required=True)
    class Meta:
        model = Slot
        fields = '__all__'
        widgets = {
            'from_time': forms.TimeInput(attrs={'type':'time'}),
            'to_time': forms.TimeInput(attrs={'type':'time'}),
        }


class LocationForm(ModelForm):
    pincode = forms.IntegerField(min_value=111111,max_value=999999)
    class Meta:
        model = Location
        fields = '__all__'
        widgets = {
            'opening_time': forms.TimeInput(attrs={'type':'time'}),
            'closing_time': forms.TimeInput(attrs={'type':'time'}),
        }


class MedicineForm(ModelForm):
    class Meta:
        model = Medicine
        fields = '__all__'
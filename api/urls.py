from django.urls import path
from .views import *


urlpatterns = [
    path('get_locations/<str:pincode>',get_locations,name='api-get-locations'),
    path('get_slots/<int:id>/<str:date>',get_slots,name="api-get-slots"),
    path('get_dose/<int:aadhar>',get_dose,name="api-get-dose"),
    path('get_available_dates/<int:id>',get_available_dates,name="api-get-slots"),
    path('get_available_medicines/<int:id>',get_available_medicines,name="api-get-medicines")
]
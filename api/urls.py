from django.urls import path
from .views import *


urlpatterns = [
    path('get_locations/<str:pincode>',get_locations,name='api-get-locations'),
    path('get_slots/<int:id>',get_slots,name="api-get-slots"),
    path('get_dose/<int:aadhar>',get_dose,name="api-get-dose"),
]
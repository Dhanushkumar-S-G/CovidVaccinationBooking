from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard,name='admin-dashboard'),

    #slots
    path('create_slot/',create_slot,name='create-slot'),
    path('edit_slot/<int:id>/',edit_slot,name='edit-slot'),
    path('delete_slot/<int:id>/',delete_slot,name='delete-slot'),

    #locations
    path('add_location/',add_location,name='add-location'),
    path('edit_location/<int:id>',edit_location,name='edit-location'),
    path('delete_location/<int:id>/',delete_location,name='delete-location'),
    path('location_stats/',location_stat,name='location-stats'),

    #medicines
    path('add_medicine/',add_medicine,name='add-medicine'),
    path('edit_medicine/<int:id>/',edit_medicine,name='edit-medicine'),
    path('delete_medicine/<int:id>/',delete_medicine,name='delete-medicine'),


    #doses
    path('add_doses/',add_dose,name='add-dose'),
    path('edit_doses/<int:id>/',edit_dose, name="edit-dose"),
    path('delete_doses/<int:id>/',delete_dose, name="delete-dose"),

    #appointments
    path('view_appointments/',view_appointments, name="view-appointments"),
    path('update_appointment/<int:id>',update_appointment,name='update-appointment')
]
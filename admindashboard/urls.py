from django.urls import path
from .views import *

urlpatterns = [
    path('dashboard/',dashboard,name='admin-dashboard'),

    #slots
    path('create_slot/',create_slot,name='create-slot'),
    path('edit_slot/<int:id>/',edit_slot,name='edit-slot'),

    #locations
    path('add_location/',add_location,name='add-location'),
    path('edit_location/<int:id>',edit_location,name='edit-location'),

    #medicines
    path('add_medicine/',add_medicine,name='add-medicine'),
    path('edit_medicine/<int:id>/',edit_medicine,name='edit-medicine'),
]
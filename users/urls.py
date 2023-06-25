from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home-page'),
    path('signup/',signup,name='signup'),
    path('logout/',user_logout,name='logout'),
    path('book_vaccination/',book_vaccination,name='book-vaccination'),
    path('view_booked/',view_booked,name='view-booked'),
    path('view_bookings/',view_bookings,name='view-bookings'),
    path('cancel_bookings/<int:id>',cancel_bookings,name='cancel-bookings'),
    
]
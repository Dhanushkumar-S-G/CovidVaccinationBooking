from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home-page'),
    path('signup/',signup,name='signup'),
    path('logout/',user_logout,name='logout'),
    path('book_vaccination/',book_vaccination,name='book-vaccination')
    
]
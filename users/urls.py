from django.urls import path
from .views import *

urlpatterns = [
    path('',home,name='home-page'),
    path('signup/',signup,name='signup'),
]
from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from admindashboard.permissions import is_admin
from django.contrib.auth.decorators import login_required
from .models import Vaccinator
from admindashboard.models import Dose,Appointment,Slot,Location
from datetime import datetime
from django.db.models import Q


def home(request):
    return render(request,"users/home.html")


def signup(request):
    if request.method == "POST":
        user = None 
        if 'LoginForm' in request.POST:
            email = request.POST.get('loginemail')
            password = request.POST.get('loginpassword')
            user = authenticate(request, username=email, password=password)

        else:
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            password = request.POST.get('password')
            user = User.objects.create_user(username=email,email=email,first_name=first_name,last_name=last_name,password=password)
            messages.success(request,"User Created successfully")
        

        if user is not None:
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request,f"User logged in {request.user}")
        else:
            messages.error(request, "Invalid Credentials")
            
    print(request.user)
    if not request.user.is_anonymous:
        if is_admin(request.user):
            return redirect('admin-dashboard')
        return redirect('home-page')
    
    return render(request,"users/signup.html")


def user_logout(request):
    logout(request)
    return redirect('home-page')


@login_required
def book_vaccination(request):
    if request.method == "POST":
        'v_name', 'v_aadhar_number', 'v_dob', 'v_mobile', 'v_gender', 'pincode', 'selectLocation', 'selectDate', 'selectSlot'
        v_aadhar_number = request.POST.get('v_aadhar_number')
        v_name = request.POST.get('v_name')
        v_dob = request.POST.get('v_dob')
        v_mobile = request.POST.get('v_mobile')
        v_gender = request.POST.get('v_gender')


        if Vaccinator.objects.filter(aadhar_number=v_aadhar_number).exists():
            vaccinator = Vaccinator.objects.get(aadhar_number = v_aadhar_number)
        else:
            vaccinator = Vaccinator.objects.create(name=v_name,dob=v_dob,aadhar_number=v_aadhar_number,mobile_number=v_mobile,gender=v_gender)

        #checking if the use has already booked an appointment
        if Appointment.objects.filter(booked_for = vaccinator,appointment_status = Appointment.BOOKED).exists():
            messages.error(request, "Vaccinator already has booked an appointment...")
            return redirect('book-vaccination')


        appointment_date = request.POST.get("selectDate")
        date = datetime.strptime(appointment_date,"%d-%m-%Y").date()
        appointment_slot = request.POST.get("selectSlot")
        appointment_location = request.POST.get("selectLocation")

        
        if Appointment.objects.filter(Q(location__id = appointment_location) & Q(appointment_date=date)  &Q(booked_slot__id = appointment_slot)).exclude(appointment_status=Appointment.CANCELED).exists():
            messages.error(request,"Sorry, this slot has been booked by another vaccinator")
            return redirect('book-vaccination')
        else:
            appointment_slot = Slot.objects.get(id=int(appointment_slot))
            appointment_location = Location.objects.get(id=int(appointment_location))
            appointment = Appointment.objects.create(booked_by=request.user,booked_for=vaccinator,appointment_date=date,booked_slot = appointment_slot,location=appointment_location)
            if vaccinator.last_put_dose:
                appointment.dose_booked_for = vaccinator.last_put_dose.next.first()
                appointment.save()
            else:
                dose = Dose.objects.filter(prev__isnull=True).first()
                appointment.dose_booked_for = dose
                appointment.save()
        messages.success(request, "Slot Booked Successfully..")
    return render(request, "users/book_vaccination.html")
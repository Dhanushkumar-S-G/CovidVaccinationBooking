from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required,user_passes_test
from .permissions import is_admin
from .forms import *
from django.contrib import messages
from datetime import datetime,timedelta
from sentry_sdk import capture_exception


@login_required
@user_passes_test(is_admin)
def dashboard(request):
    try:
        today = datetime.now().date()
        labels = []
        booked = []
        visitied = []

    
        for i in range(10,-1,-1):
            current_date = today - timedelta(days=i)
            labels.append(current_date.strftime("%d-%b"))

            appointments = Appointment.objects.filter(appointment_date=current_date)
            booked.append(appointments.count())

            visitied_app = appointments.filter(appointment_status=Appointment.VACCINATED)
            visitied.append(visitied_app.count())


        total_booked = Appointment.objects.filter(appointment_status=Appointment.BOOKED).count()
        total_vaccinated = Appointment.objects.filter(appointment_status=Appointment.VACCINATED).count()
        total_canceled = Appointment.objects.filter(appointment_status=Appointment.CANCELED).count()
        total_expired = Appointment.objects.filter(appointment_status=Appointment.EXPIRED).count()

        total_data = [total_booked,total_vaccinated,total_canceled,total_expired]

        return render(request, "admindashboard/dashboard.html",{
            'labels':labels,
            'booked':booked,
            'visited':visitied,
            'total_data':total_data
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


#slot related
@login_required
@user_passes_test(is_admin)
def create_slot(request):
    try:
        if request.method == 'POST':
            form = SlotForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Slot created Successfully..")
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")
        form = SlotForm()
        available_slots = Slot.objects.all()
        return render(request,'admindashboard/slots.html',{
            'form':form,
            'available_slots' : available_slots,
            })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')

@login_required
@user_passes_test(is_admin)
def edit_slot(request,id):

    try:
        slot = Slot.objects.get(id=id)

        if request.method == 'POST':
            form = SlotForm(request.POST,instance=slot)
            if form.is_valid():
                form.save()
                messages.success(request, "Slot updated Successfully..")
                return redirect('create-slot')
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")


        form = SlotForm(instance=slot)
        return render(request,'admindashboard/edit_slot.html',{
            'form':form
            })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


@login_required
@user_passes_test(is_admin)
def delete_slot(request,id):
    try:
        slot = Slot.objects.get(id=id)
        slot.delete()
        messages.success(request, "Slot deleted successfully")
        return redirect('add-slot')
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


#location related
@login_required
@user_passes_test(is_admin)
def add_location(request):
    try:
        if request.method == "POST":
            form = LocationForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, "Locations added Successfully.")
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")

        form = LocationForm()
        locations = Location.objects.all()

        return render(request, "admindashboard/add_location.html",{
            'form':form,
            'locations':locations
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')



@login_required
@user_passes_test(is_admin)
def edit_location(request,id):
    try:
        location = Location.objects.get(id=id)

        if request.method == "POST":
            form = LocationForm(request.POST,instance=location)
            if form.is_valid():
                form.save()
                messages.success(request, "Location updated Successfully.")
                return redirect('add-location')
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")

        form = LocationForm(instance=location)
        locations = Location.objects.all()

        return render(request, "admindashboard/edit_location.html",{
            'form':form,
            'locations':locations
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


@login_required
@user_passes_test(is_admin)
def delete_location(request,id):
    try:

        location = Location.objects.get(id=id)
        location.delete()
        messages.success(request, "Location object deleted successfully..")
        return redirect('add-location')
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


#medicine related
@login_required
@user_passes_test(is_admin)
def add_medicine(request):
    try:
        if request.method == 'POST':
            form = MedicineForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Medicine object created successfully..")
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")
        
        medicines = Medicine.objects.all()
        form = MedicineForm()
        return render(request, "admindashboard/add_medicine.html",{
            'form':form,
            'medicines':medicines,
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


@login_required
@user_passes_test(is_admin)
def edit_medicine(request,id):
    try:
        medicine = Medicine.objects.get(id=id)

        if request.method == 'POST':
            form = MedicineForm(request.POST,instance=medicine)
            if form.is_valid():
                form.save()
                messages.success(request,"Medicine object updated successfully..")
                return redirect('add-medicine')
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")

        form = MedicineForm(instance=medicine)

        return render(request, "admindashboard/edit_medicine.html",{
            'form':form,
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


@login_required
@user_passes_test(is_admin)
def delete_medicine(request,id):
    try:

        medicine = Medicine.objects.get(id=id)
        medicine.delete()
        messages.success(request, "Medicine object deleted successfully..")
        return redirect('add-medicine')
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')



#dose related
@login_required
@user_passes_test(is_admin)
def add_dose(request):
    try:
        if request.method == "POST":
            form = DoseForm(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request,"Dose object created successfully..")
                return redirect('add-dose')
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")

        form = DoseForm()
        doses = Dose.objects.all()
        return render(request, "admindashboard/add_dose.html",{
            'form':form,
            'doses':doses,
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


@login_required
@user_passes_test(is_admin)
def edit_dose(request,id):
    try:
        dose = Dose.objects.get(id=id)

        if request.method == "POST":
            form = DoseForm(request.POST,instance=dose)
            if form.is_valid():
                form.save()
                messages.success(request,"Dose object updated Successfully..")
                return redirect('add-dose')
            else:
                for field,errors in form.errors.items():
                    for error in errors:
                        messages.error(request,f"Error in {field} : {error}")

                        
        form = DoseForm(instance=dose)
        return render(request, "admindashboard/edit_dose.html",{
            'form':form,
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


@login_required
@user_passes_test(is_admin)
def delete_dose(request,id):
    try:

        dose = Dose.objects.get(id=id)
        dose.delete()
        messages.success(request,"Dose object deleted")
        return redirect('add-dose')
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')


#appointments related
@login_required
@user_passes_test(is_admin)
def view_appointments(request):
    try:
        appointments = Appointment.objects.filter(appointment_status=Appointment.BOOKED,appointment_date__gte = datetime.now().date())
        return render (request, "admindashboard/view_appointments.html",{
            'appointments' : appointments
        })
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')

@login_required
@user_passes_test(is_admin)
def update_appointment(request,id):
    try:

        appointment = Appointment.objects.get(id=id)
        appointment.appointment_status = Appointment.VACCINATED
        appointment.save()
        messages.success(request, "Vaccinator details updated successfully..")
        return redirect('view-appointments')
    
    except Exception as e:
        capture_exception(e)
        messages.error(request, "An unknown error has occured")
        return redirect('admin-dashboard')

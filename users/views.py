from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from admindashboard.permissions import is_admin


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


def book_vaccination(request):
    if request.method == "POST":
        print(request.POST.keys())
    return render(request, "users/book_vaccination.html")
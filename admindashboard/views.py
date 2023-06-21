from django.shortcuts import render
from django.contrib.auth.decorators import login_required,user_passes_test
from .permissions import is_admin


@login_required
# @user_passes_test(is_admin)
def dashboard(request):

    return render(request, "admindashboard/dashboard.html")

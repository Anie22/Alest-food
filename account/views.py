from multiprocessing import context
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
# from home.apps.homeConfig import urls

# Create your views here.

def login_view(request):
    if request.method == "POST":
       username = request.POST.get("username")
       password = request.POST.get("password")
       user = authenticate(request, username=username, password=password)
       if user is not None:
           login(request,user)
           return redirect("home:home")
    return render(request, "home/login.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        password1 = request.POST.get("password")
        password2 = request.POST.get("confirm_password")
        
        if password2 == password1:
           new_user = User.objects.create_user(username=username, email=email, first_name=fname, last_name=lname, password=password1)
           new_user.save()
        return redirect("home:login")
    return render(request, "home/register.html")

def logout_view(request):
    logout(request)
    return redirect("home:home")
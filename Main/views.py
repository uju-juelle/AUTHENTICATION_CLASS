from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse
from django.contrib import messages
from django.contrib import auth


def home(request):
    return render(request, "Main/home.html")

def register(request):
    if request.method =="POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            messages.success(request, f"Hello {username}, Your account has been created, Kindly sign in below")
            return redirect("login")
            # return HttpResponse("Your account has been created")
        
    elif request.method == "GET":
        form = UserRegistrationForm()

    context = {
        "form": form
    }
    return render(request, "Main/register.html", context)



def frontend_register(request):
    if request.method == "POST":
        new_username = request.POST["username"]
        new_email = request.POST["email"]
        new_password = request.POST["password1"]
        new_password2 = request.POST["password2"]

        if new_password == new_password2:
            if User.objects.filter(username=new_username).exists():
                messages.error(request, "User already exists")
                return redirect("register")
            elif User.objects.filter(email=new_email).exists():
                messages.error(request, "That email has been taken")
                return redirect("register")
            else:
                User.objects.create_user(username=new_username, email=new_email, password=new_password)
                messages.success(request, "Your account has been created successfully")
                return redirect("login")
        else:
            messages.error(request, "Both passwords must match")
            return redirect("register")
    else:
        return render(request, "Main/frontend_registration.html") 
    

def frontend_login(request):
        if request.method == "POST":
            username = request.POST["username"]
            password = request.POST["password"]

            user = auth.authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect("/")
            
            else: 
                messages.error(request,"invalid credentials supplied")
                return redirect("login")
            
        else:
            return render(request, "Main/frontend_login.html")
        


def frontend_logout(request):
    auth.logout(request)
    return redirect("/")
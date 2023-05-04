from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, "home.html")


# AUTHENTICATION APIs
def handleSignup(request):
    if request.method == "POST":
        # Get the post parameters
        name = request.POST["name"]
        email = request.POST["email"]
        password = request.POST["password"]
        rpassword = request.POST["rpassword"]

        # Create the user
        myuser = User.objects.create_user(
            username=name, email=email, password=rpassword
        )
        myuser.save()
        return render(request, "login.html")
    return render(request, "login.html")


def handleLogin(request):
    if request.method == "POST":
        name = request.POST["name"]
        password = request.POST["password"]
        user = authenticate(username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect("archive")
        else:
            return redirect("archive")
    return render(request, "login.html")


def handleLogout(request):
    logout(request)
    return redirect("/")

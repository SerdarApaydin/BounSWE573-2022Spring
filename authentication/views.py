from ast import If
from telnetlib import LOGOUT
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from learningspace import settings
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request, 'authentication/index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["eaddress"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        if User.objects.filter(username=username):
            messages.error(request, "Username already exist. Please try another username.")
            return redirect('home')

        if User.objects.filter(email=email):
            messages.error(request, "Email address is already in use. Please try another email address.")
            return redirect('home')

        if len(username)>12:
            messages.error(request, "Username must be under 12 characters.")

        if pass1 != pass2:
            messages.error(request, "Passwords don't match.")

        if not username.isalnum():
            messages.error(request, "Username must be Alpha-Numeric.")

        siteUser = User.objects.create_user(username, email, pass1)

        siteUser.save()

        messages.success(request, "Your account has been successfully created. We have sent you a confirmation email, please confirm your email to activate your account.")

        # Welcome Email

        subject = "Welcome to LearnCommune!"
        message = "Hello" + siteUser.username + ", \n\n" + "Welcome to LearnCommune! \n Thank you for joining us. \n We have sent you a confirmation email, please confirm your email address to activate your account. \n\n Thank you"
        from_email = settings.EMAIL_HOST_USER
        to_list = [siteUser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)

        return redirect('signin')

    return render(request, 'authentication/signup.html')

def signin(request):

    if request.method == "POST":
        username = request.POST["username"]
        pass1    = request.POST["pass1"]

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            username = user.username
            return render(request, "authentication/index.html", {'username': username})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect('home')


    return render(request, 'authentication/signin.html')

def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')
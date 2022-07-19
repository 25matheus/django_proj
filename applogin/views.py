import email
from wsgiref.util import request_uri
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    return render(request, "authentication/index.html")
def signup(request):
    if request.method == "POST":
        #Getting the sign up info from the user via POST to create a new user
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        myuser = User.objects.create_user(username, email, password1)
        myuser.first_name = firstname
        myuser.last_name = lastname
        myuser.save()

        messages.success(request, "Your account has been created!")
        return redirect("signin")
    return render(request, "authentication/signup.html")

def signin(request):
    if request.method == "POST":
        username = request.POST['username']
        password1 = request.POST['password1']

        user = authenticate(username=username, password=password1)

        if user is not None:
            login(request, user)
            firstname = user.first_name
            return render(request, "authentication/index.html", {'fname':firstname}) #passing the first name to the index page to be used with the Hello message
        else:
            messages.error(request, "incorrect credentials")
            return redirect('home')
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request) # imported from logout
    messages.success(request, "Logged Out")
    return redirect('home')
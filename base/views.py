from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib import messages

from blogs.models import Blog 

# Create your views here.

def home(request):
    recent_blogs = Blog.objects.all()[0:6]
    context = {
        "recent_blogs":recent_blogs,
    }
    return render(request, "base/home.html",context)


def sign_up(request):
    redirect_link = request.GET.get("next")

    if request.user.is_authenticated:
        return redirect("home")
    if request.method == "POST":
        first_name = request.POST["first-name"]
        last_name = request.POST["last-name"]
        username = request.POST["username"]
        email = request.POST["email"]
        password1 = request.POST["password1"]
        password2 = request.POST["password2"]

        # cleaning the form data
        if password1 == password2:
            if len(password1) <= 4 or len(password2) <= 4:
                messages.error(request,"Your Password Is too Short")
                return redirect("sign-up")
            if User.objects.filter(email = email).exists():
                messages.error(request,"This Email Is Already In Use")
                return redirect("sign-up")
            if User.objects.filter(username = username).exists():
                messages.error(request,"This Username Has Been Taken")
                return redirect("sign-up")
        else:
            messages.error(request,"OOps! Your Passwords Don't Match")
            return redirect("sign-up")
        
        # create a user with the cleaned form data
        user = User.objects.create_user(username = username,password = password1,first_name = first_name, last_name = last_name, email = email)
        user.save()
        if redirect_link != None:
            return redirect(redirect_link)
        login(request,user)
        return redirect("home")
    
    return render(request,"base/sign-up.html")


def Login(request):
    redirect_link = request.GET.get("next")
    
    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request,user)
            if redirect_link != None:
                return redirect(redirect_link)
            return redirect("home")
        else:
            messages.error(request,"Invalid Credentials")
    return render(request,"base/login.html")


def Logout(request):
    logout(request)
    return redirect("home")


def contact(request):
    return render(request,"base/contact.html")
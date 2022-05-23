from django.http import HttpResponseNotFound
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.paginator import Paginator

from .models import Profile, Subscribers
from .forms import ProfileForm
from blogs.models import Blog

# Create your views here.

@login_required(login_url="login")
def profile_page(request,id):
    """
        gets a user's blog's profile and listens for post request to add other users to the profile user's subscribers list
    """

    profile_user = User.objects.get(id = id)
    try:
        profile = Profile.objects.get(user = profile_user)
    except:
        if request.user == profile_user:
            return redirect("create-profile")
        else:
            return HttpResponseNotFound()
    
    # checking if the request user is a follower of this profile user
    user_subscribers_account,created = Subscribers.objects.get_or_create(user = profile_user)
    is_a_subscriber = user_subscribers_account.is_a_subscriber(request.user)
    
    # getting the profile user blogs and subscribers
    if Blog.objects.filter(user = profile_user).exists():
        all_profile_user_blogs = Blog.objects.filter(user = profile_user)
        latest_blogs = all_profile_user_blogs[0:3]
    else:
        latest_blogs = ""
        all_profile_user_blogs =""

    subscribers = len(user_subscribers_account.subscribed.all())
    subscribed_to = len(Subscribers.objects.filter(subscribed = profile_user))

    context = {
        "profile":profile,
        "blogs": latest_blogs,
        "lob":len(all_profile_user_blogs),
        "is_a_follower":is_a_subscriber,
        "subscribers":subscribers,
        "subscribed_to":subscribed_to,
    }
    return render(request,"account/profile.html",context)


def all_profile_blogs(request,id):
    user = User.objects.get(id = id)
    blogs = Blog.objects.filter(user = user)

    #show 6 blogs per page
    paginator = Paginator(blogs,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "profile_user":user,
        "blogs":blogs,
        "lob":len(blogs),
        "page":page_obj
    }
    return render(request,"account/all-user-blogs.html",context)


@login_required(login_url="login")
def create_profile(request):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            dummy = form.save(commit = False)
            dummy.user = request.user
            dummy.save()
        return redirect("account",request.user.id)
    context = {"form":form}
    return render(request,"account/create-profile.html",context)


@login_required(login_url="login")
def update_profile(request):
    try:
        profile = Profile.objects.get(user = request.user)
    except:
        return HttpResponseNotFound()

    form = ProfileForm(instance = profile)
    if request.method == "POST":
        form = ProfileForm(request.POST,request.FILES,instance = profile)

        if form.is_valid():
            form.save()
            return redirect("account",request.user.id)
    context = {
        "form":form,
    }
    return render(request,"account/update-profile.html",context)


#### subscribe functionalities #######
@login_required(login_url="login")
def subscribe(request,id):
    # subscribe logic
    profile_user = User.objects.get(id = id)
    user_subscribers_account,created = Subscribers.objects.get_or_create(user = profile_user)
    if request.method == "POST":
        user_subscribers_account.subscribed.add(request.user)
        return redirect("account", profile_user.id)